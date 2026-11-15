"""Junk Bag mark v6: an egg-shaped bin bag with a flat bottom, a rounded collar at the neck and a tall gathered
top with a peak and one pointed end; highlights and the collar gaps are cut out (negative space). The minimal
burger, unchanged, sits inside.

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

# ---- the bag (512 grid) ----
BODY = ('M208 200 C126 222 82 324 80 408 C79 456 100 480 140 482 L372 482 C412 480 433 456 432 408 '
        'C430 324 386 222 304 200 Z')
COLLAR = 'M214 172 Q256 160 298 172 Q308 184 300 200 Q256 210 212 200 Q204 184 214 172 Z'
TOP = ('M224 170 C216 132 210 94 204 52 C222 64 238 72 254 68 C270 64 284 56 298 50 '
       'C302 82 306 108 314 128 C338 132 362 138 376 150 C344 160 314 166 290 170 Z')
K, CX, CY = 0.58, 244, 372   # burger scale and centre inside the bag

def cuts():
    """Negative space on the bag: collar gaps, highlights."""
    st = 'fill="none" stroke="#000" stroke-linecap="round"'
    return (f'<path d="M210 200 Q256 212 302 200" {st} stroke-width="9"/>'          # gap between collar and body
            f'<path d="M218 170 Q256 158 294 170" {st} stroke-width="8"/>'          # gap between top and collar
            f'<path d="M226 76 C234 104 238 130 236 150 C230 128 224 102 220 80 Z" fill="#000"/>'   # highlight, left peak
            f'<path d="M296 112 C286 128 276 144 268 158 C280 146 292 132 304 120 Z" fill="#000"/>'  # highlight, right end
            f'<path d="M346 240 C384 296 404 364 398 436" {st} stroke-width="14"/>')  # long highlight on the body

def mark(fill=INK, line=WHITE, cheese=AMBER, p=''):
    m = (f'<defs><mask id="{p}cut" maskUnits="userSpaceOnUse" x="0" y="0" width="512" height="512">'
         f'<rect width="512" height="512" fill="#fff"/>{cuts()}</mask></defs>')
    sil = (f'<g mask="url(#{p}cut)" fill="{fill}" stroke="{fill}" stroke-width="10" stroke-linejoin="round">'
           f'<path d="{TOP}"/><path d="{COLLAR}"/><path d="{BODY}"/></g>')
    bg = f'<g transform="translate({CX - 256*K:.1f} {CY - 330*K:.1f}) scale({K})">{burger(fill, line, cheese, p)}</g>'
    return m + sil + bg

def svg(vb, body, label='Junkbox'):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{label}"><title>{label}</title>{body}</svg>\n'
def write(name, s): open(os.path.join(OUT, name), 'w').write(s); print('wrote', name)

# ---- lockups with Junkbox's own hand lettering ----
TR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'trace')
WORD = open(os.path.join(TR, 'd-word.txt')).read(); TAG = open(os.path.join(TR, 'd-tag.txt')).read()
WB = (769, 316, 2208, 548); TB = (516, 2644, 2564, 2721)
MB = (72, 42, 440, 490)  # mark bounds on the 512 grid
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

stacked('junkbag-v6-stacked-on-amber.svg', AMBER, INK)
stacked('junkbag-v6-stacked-on-ink.svg', INK, AMBER, fill=AMBER, line=INK, cheese=WHITE)
stacked('junkbag-v6-stacked-on-white.svg', None, INK)
horizontal('junkbag-v6-horizontal-on-amber.svg', AMBER, INK)
horizontal('junkbag-v6-horizontal-on-white.svg', None, INK)
avatar('junkbag-v6-avatar.svg')
write('junkbag-v6-mark-on-amber.svg', svg('0 0 512 512', f'<rect width="512" height="512" fill="{AMBER}"/>' + mark()))
write('junkbag-v6-mark.svg', svg('0 0 512 512', mark()))
write('junkbag-v6-mark-on-ink.svg', svg('0 0 512 512', f'<rect width="512" height="512" fill="{INK}"/>' + mark(fill=AMBER, line=INK, cheese=WHITE)))
