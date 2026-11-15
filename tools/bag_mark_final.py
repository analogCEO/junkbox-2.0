"""Junk Bag mark, final direction: the minimal burger, unchanged, inside a more recognisable bin bag top
(pinched gathered neck, tie band, two pointed asymmetric tie ends, small knot): one ink silhouette on amber, softer shapes, and a white inline
contour inside the edge, with the burger drawn inside in white lines (plus amber cheese).

Usage: python3 bag_mark_round.py <out dir>
"""
import os, sys
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
INK, AMBER, WHITE = '#231F20', '#F7AF0B', '#FFFFFF'

BODY = ('M226 178 C166 184 102 222 96 292 C92 334 94 380 98 414 C102 462 146 484 198 482 '
        'C232 480 280 480 314 482 C366 484 410 462 414 414 C418 380 420 334 416 292 C410 222 346 184 286 178 Z')
NECK = 'M206 192 C228 184 238 160 240 136 L272 136 C274 160 284 184 306 192 Z'
EAR_L = 'M248 136 L214 112 L178 80 L172 66 L186 70 L190 56 L202 62 L212 50 L224 66 L244 100 L262 128 Z'
EAR_R = 'M262 136 L298 120 L338 108 L350 100 L344 90 L356 84 L348 74 L358 64 L340 64 L306 88 L264 124 Z'
KNOT = (256, 132, 16)
ROUND = 16  # same-colour stroke that rounds every corner of the silhouette

def inline(d, cid, gap, w, fill, line=WHITE):
    """White line running inside the edge of shape d, `gap` px in, `w` px thick (plus the rounding stroke)."""
    return (f'<clipPath id="{cid}"><path d="{d}"/></clipPath>'
            f'<g clip-path="url(#{cid})"><path d="{d}" fill="none" stroke="{line}" stroke-width="{2*(gap+w)}" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="{fill}" stroke-width="{2*gap}" stroke-linejoin="round"/></g>')

def wave(y, x0=80, x1=432, amp=8, period=34):
    n = int((x1 - x0) / (period / 2)); d = f'M{x0} {y}'
    for i in range(n):
        d += f' Q{x0 + (i + .5) * period / 2:.1f} {y + (amp if i % 2 else -amp)} {x0 + (i + 1) * period / 2:.1f} {y}'
    return d

def mark(fill=INK, line=WHITE, cheese=AMBER, p=''):
    sil = (f'<g fill="{fill}" stroke="{fill}" stroke-width="{ROUND}" stroke-linejoin="round">'
           f'<path d="{NECK}"/><path d="{BODY}"/></g>'
           f'<g fill="{fill}" stroke="{fill}" stroke-width="6" stroke-linejoin="round"><path d="{EAR_L}"/><path d="{EAR_R}"/></g>'
           f'<circle cx="{KNOT[0]}" cy="{KNOT[1]}" r="{KNOT[2]}" fill="{fill}"/>')
    s = f'stroke="{line}" stroke-linecap="round" stroke-linejoin="round" fill="none"'
    seeds = ''.join(f'<ellipse cx="{x}" cy="{y}" rx="17" ry="10" fill="{line}" transform="rotate({r} {x} {y})"/>'
                    for x, y, r in [(198, 268, -18), (258, 252, 0), (318, 268, 18)])
    lettuce = f'<path d="{wave(318, amp=13, period=58)}" {s} stroke-width="14"/>'
    drips = (f'<path d="M80 336 L432 336 L432 352 L350 352 C350 352 350 384 334 384 C318 384 318 352 318 352 '
             f'L276 352 C276 352 276 402 256 402 C236 402 236 352 236 352 L196 352 C196 352 196 380 182 380 C168 380 168 352 168 352 L80 352 Z" fill="{cheese}"/>')
    bottom = f'<path d="M80 418 L432 418" {s} stroke-width="14"/>'
    details = f'<g clip-path="url(#{p}bodyc)">{lettuce}{drips}{bottom}{seeds}</g>'
    body_inline = inline(BODY, f'{p}bodyc', 13, 11, fill, line)
    seal = f'<g fill="none" stroke="{fill}" stroke-width="{ROUND + 6}" stroke-linejoin="round"><path d="{BODY}"/></g>'
    tie = (f'<path d="M240 144 Q256 150 272 144" {s} stroke-width="9"/>'
           f'<path d="M246 156 L232 184 M256 158 L256 186 M266 156 L280 184" {s} stroke-width="6"/>')
    return sil + f'<defs><clipPath id="{p}bodyc"><path d="{BODY}"/></clipPath></defs>' + details + body_inline.replace(f'<clipPath id="{p}bodyc"><path d="{BODY}"/></clipPath>', '') + seal + tie

def svg(vb, body, label='Junkbox'):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{label}"><title>{label}</title>{body}</svg>\n'
def write(name, s): open(os.path.join(OUT, name), 'w').write(s); print('wrote', name)

# ---------------- lockups with Junkbox's own hand lettering ----------------
TR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'trace')
WORD = open(os.path.join(TR, 'd-word.txt')).read(); TAG = open(os.path.join(TR, 'd-tag.txt')).read()
WB = (769, 316, 2208, 548); TB = (516, 2644, 2564, 2721)
MB = (82, 48, 430, 498)  # mark bounds on the 512 grid, rounding stroke included
def placed(d, b, x, y, w, fill):
    k = w / (b[2] - b[0])
    return f'<path fill-rule="evenodd" fill="{fill}" transform="translate({x - b[0]*k:.2f} {y - b[1]*k:.2f}) scale({k:.5f})" d="{d}"/>', (b[3] - b[1]) * k
def mark_at(x, y, h, pfx, **kw):
    k = h / (MB[3] - MB[1])
    return f'<g transform="translate({x - MB[0]*k:.2f} {y - MB[1]*k:.2f}) scale({k:.4f})">{mark(p=pfx, **kw)}</g>', (MB[2] - MB[0]) * k
def stacked(name, bg, txt, **kw):
    W, pad, mh = 1000, 100, 480
    g, mw = mark_at((W - 0) / 2, pad, mh, 's', **kw)
    g = g.replace('translate(', f'translate({-mw/2:.2f} 0) translate(', 1)
    word, hw = placed(WORD, WB, (W - 560) / 2, pad + mh + 64, 560, txt)
    tag, ht = placed(TAG, TB, (W - 600) / 2, pad + mh + 64 + hw + 40, 600, txt)
    H = pad + mh + 64 + hw + 40 + ht + pad
    rect = f'<rect width="{W}" height="{H:.0f}" fill="{bg}"/>' if bg else ''
    write(name, svg(f'0 0 {W} {H:.0f}', rect + g + word + tag))
def horizontal(name, bg, txt, **kw):
    pad, mh = 60, 310
    g, mw = mark_at(pad, pad, mh, 'h', **kw)
    tx = pad + mw + 56
    word, hw = placed(WORD, WB, tx, pad + 96, 560, txt)
    tag, ht = placed(TAG, TB, tx, pad + 96 + hw + 34, 560, txt)
    W, H = tx + 560 + pad, mh + 2 * pad
    rect = f'<rect width="{W:.0f}" height="{H}" fill="{bg}"/>' if bg else ''
    write(name, svg(f'0 0 {W:.0f} {H}', rect + g + word + tag))
def avatar(name):
    g, mw = mark_at(0, 0, 340, 'a')
    g = f'<g transform="translate({(512 - mw)/2:.1f} {(512 - 340)/2:.1f})">{g}</g>'
    write(name, svg('0 0 512 512', f'<rect width="512" height="512" fill="{AMBER}"/>{g}'))

stacked('junkbag-final-stacked-on-amber.svg', AMBER, INK)
stacked('junkbag-final-stacked-on-ink.svg', INK, AMBER, fill=AMBER, line=INK, cheese=WHITE)
stacked('junkbag-final-stacked-on-white.svg', None, INK)
horizontal('junkbag-final-horizontal-on-amber.svg', AMBER, INK)
horizontal('junkbag-final-horizontal-on-white.svg', None, INK)
avatar('junkbag-final-avatar.svg')
write('junkbag-final-mark-on-amber.svg', svg('0 0 512 512', f'<rect width="512" height="512" fill="{AMBER}"/>' + mark()))
write('junkbag-final-mark.svg', svg('0 0 512 512', mark()))
write('junkbag-final-mark-on-ink.svg', svg('0 0 512 512', f'<rect width="512" height="512" fill="{INK}"/>' + mark(fill=AMBER, line=INK, cheese=WHITE)))
