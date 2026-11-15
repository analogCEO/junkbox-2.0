"""Junk Bag mark v5: a classic bin-bag silhouette (wide sagging bottom, tapering shoulders, pinched neck,
knot, two big pointed tie ends) with the minimal burger, unchanged, sitting smaller inside it.

Usage: python3 bag_mark_v5.py <out dir>
"""
import os, sys
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
INK, AMBER, WHITE = '#231F20', '#F7AF0B', '#FFFFFF'

# ---- the burger, exactly as in the minimal version (512 grid) ----
BURGER = ('M226 178 C166 184 102 222 96 292 C92 334 94 380 98 414 C102 462 146 484 198 482 '
          'C232 480 280 480 314 482 C366 484 410 462 414 414 C418 380 420 334 416 292 C410 222 346 184 286 178 Z')

def wave(y, x0=80, x1=432, amp=13, period=58):
    n = int((x1 - x0) / (period / 2)); d = f'M{x0} {y}'
    for i in range(n):
        d += f' Q{x0 + (i + .5) * period / 2:.1f} {y + (amp if i % 2 else -amp)} {x0 + (i + 1) * period / 2:.1f} {y}'
    return d

def burger(fill, line, cheese, p):
    s = f'stroke="{line}" stroke-linecap="round" stroke-linejoin="round" fill="none"'
    seeds = ''.join(f'<ellipse cx="{x}" cy="{y}" rx="17" ry="10" fill="{line}" transform="rotate({r} {x} {y})"/>'
                    for x, y, r in [(198, 268, -18), (258, 252, 0), (318, 268, 18)])
    lettuce = f'<path d="{wave(318)}" {s} stroke-width="14"/>'
    drips = (f'<path d="M80 336 L432 336 L432 352 L350 352 C350 352 350 384 334 384 C318 384 318 352 318 352 '
             f'L276 352 C276 352 276 402 256 402 C236 402 236 352 236 352 L196 352 C196 352 196 380 182 380 C168 380 168 352 168 352 L80 352 Z" fill="{cheese}"/>')
    bottom = f'<path d="M80 418 L432 418" {s} stroke-width="14"/>'
    gap, w = 13, 11
    return (f'<defs><clipPath id="{p}bc"><path d="{BURGER}"/></clipPath></defs>'
            f'<g clip-path="url(#{p}bc)">{lettuce}{drips}{bottom}{seeds}'
            f'<path d="{BURGER}" fill="none" stroke="{line}" stroke-width="{2*(gap+w)}"/>'
            f'<path d="{BURGER}" fill="none" stroke="{fill}" stroke-width="{2*gap}"/></g>'
            f'<path d="{BURGER}" fill="none" stroke="{fill}" stroke-width="10"/>')

# ---- the bag (512 grid): pear-shaped sack, pinched neck, knot, two big pointed tie ends ----
BAG = ('M232 170 C196 184 122 232 86 304 C52 372 54 444 94 476 C122 498 172 500 214 494 '
       'C234 491 246 498 256 498 C266 498 278 491 298 494 C340 500 390 498 418 476 '
       'C458 444 460 372 426 304 C390 232 316 184 280 170 Z')
NECK = 'M232 172 C240 158 242 144 238 128 L274 128 C270 144 272 158 280 172 Z'
EAR_L = 'M248 128 C222 110 176 82 120 30 C178 38 224 66 262 120 Z'
EAR_R = 'M264 128 C292 104 330 70 386 44 C356 90 312 118 266 136 Z'
KNOT = (256, 124, 18)
K, CX, CY = 0.60, 256, 382   # burger scale and centre inside the bag

def mark(fill=INK, line=WHITE, cheese=AMBER, p=''):
    sil = (f'<g fill="{fill}" stroke="{fill}" stroke-width="14" stroke-linejoin="round">'
           f'<path d="{EAR_L}"/><path d="{EAR_R}"/><path d="{NECK}"/><path d="{BAG}"/></g>'
           f'<circle cx="{KNOT[0]}" cy="{KNOT[1]}" r="{KNOT[2]}" fill="{fill}"/>')
    s = f'stroke="{line}" stroke-linecap="round" fill="none"'
    tie = f'<path d="M238 140 Q256 147 274 140" {s} stroke-width="10"/>'
    creases = f'<path d="M242 182 Q222 200 204 228 M256 186 L256 220 M270 182 Q290 200 308 228" {s} stroke-width="9"/>'
    b = f'<g transform="translate({CX - 256*K:.1f} {CY - 330*K:.1f}) scale({K})">{burger(fill, line, cheese, p)}</g>'
    return sil + tie + creases + b

def svg(vb, body, label='Junkbox'):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{label}"><title>{label}</title>{body}</svg>\n'
def write(name, s): open(os.path.join(OUT, name), 'w').write(s); print('wrote', name)

# ---- lockups with Junkbox's own hand lettering ----
TR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'trace')
WORD = open(os.path.join(TR, 'd-word.txt')).read(); TAG = open(os.path.join(TR, 'd-tag.txt')).read()
WB = (769, 316, 2208, 548); TB = (516, 2644, 2564, 2721)
MB = (46, 24, 466, 506)  # mark bounds on the 512 grid
def placed(d, b, x, y, w, fill):
    k = w / (b[2] - b[0])
    return f'<path fill-rule="evenodd" fill="{fill}" transform="translate({x - b[0]*k:.2f} {y - b[1]*k:.2f}) scale({k:.5f})" d="{d}"/>', (b[3] - b[1]) * k
def mark_at(x, y, h, pfx, **kw):
    k = h / (MB[3] - MB[1])
    return f'<g transform="translate({x - MB[0]*k:.2f} {y - MB[1]*k:.2f}) scale({k:.4f})">{mark(p=pfx, **kw)}</g>', (MB[2] - MB[0]) * k
def stacked(name, bg, txt, **kw):
    W, pad, mh = 1000, 90, 500
    k = mh / (MB[3] - MB[1]); mw = (MB[2] - MB[0]) * k
    g, _ = mark_at((W - mw) / 2, pad, mh, 's', **kw)
    word, hw = placed(WORD, WB, (W - 560) / 2, pad + mh + 60, 560, txt)
    tag, ht = placed(TAG, TB, (W - 600) / 2, pad + mh + 60 + hw + 40, 600, txt)
    H = pad + mh + 60 + hw + 40 + ht + pad
    rect = f'<rect width="{W}" height="{H:.0f}" fill="{bg}"/>' if bg else ''
    write(name, svg(f'0 0 {W} {H:.0f}', rect + g + word + tag))
def horizontal(name, bg, txt, **kw):
    pad, mh = 50, 330
    g, mw = mark_at(pad, pad, mh, 'h', **kw)
    tx = pad + mw + 50
    word, hw = placed(WORD, WB, tx, pad + 110, 560, txt)
    tag, ht = placed(TAG, TB, tx, pad + 110 + hw + 34, 560, txt)
    W, H = tx + 560 + pad, mh + 2 * pad
    rect = f'<rect width="{W:.0f}" height="{H}" fill="{bg}"/>' if bg else ''
    write(name, svg(f'0 0 {W:.0f} {H}', rect + g + word + tag))
def avatar(name):
    h = 370; k = h / (MB[3] - MB[1]); mw = (MB[2] - MB[0]) * k
    g, _ = mark_at((512 - mw) / 2, (512 - h) / 2 + 4, h, 'a')
    write(name, svg('0 0 512 512', f'<rect width="512" height="512" fill="{AMBER}"/>{g}'))

stacked('junkbag-v5-stacked-on-amber.svg', AMBER, INK)
stacked('junkbag-v5-stacked-on-ink.svg', INK, AMBER, fill=AMBER, line=INK, cheese=WHITE)
stacked('junkbag-v5-stacked-on-white.svg', None, INK)
horizontal('junkbag-v5-horizontal-on-amber.svg', AMBER, INK)
horizontal('junkbag-v5-horizontal-on-white.svg', None, INK)
avatar('junkbag-v5-avatar.svg')
write('junkbag-v5-mark-on-amber.svg', svg('0 0 512 512', f'<rect width="512" height="512" fill="{AMBER}"/>' + mark()))
write('junkbag-v5-mark.svg', svg('0 0 512 512', mark()))
write('junkbag-v5-mark-on-ink.svg', svg('0 0 512 512', f'<rect width="512" height="512" fill="{INK}"/>' + mark(fill=AMBER, line=INK, cheese=WHITE)))
