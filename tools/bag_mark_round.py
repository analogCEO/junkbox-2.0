"""Junk Bag mark, rounded version: one ink silhouette on amber, softer shapes, and a white inline
contour inside the edge, with the burger drawn inside in white lines (plus amber cheese).

Usage: python3 bag_mark_round.py <out dir>
"""
import os, sys
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
INK, AMBER, WHITE = '#231F20', '#F7AF0B', '#FFFFFF'

BODY = ('M226 178 C166 184 102 222 96 292 C92 334 94 380 98 414 C102 462 146 484 198 482 '
        'C232 480 280 480 314 482 C366 484 410 462 414 414 C418 380 420 334 416 292 C410 222 346 184 286 178 Z')
NECK = 'M230 158 Q256 166 282 158 L292 184 Q256 194 220 184 Z'
EAR_L = 'M244 140 C224 112 194 70 164 70 C138 70 134 100 158 120 C182 140 216 150 240 154 Z'
EAR_R = 'M268 140 C288 112 318 70 348 70 C374 70 378 100 354 120 C330 140 296 150 272 154 Z'
KNOT = (256, 146, 24)
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
           f'<path d="{EAR_L}"/><path d="{EAR_R}"/><path d="{NECK}"/><path d="{BODY}"/></g>'
           f'<circle cx="{KNOT[0]}" cy="{KNOT[1]}" r="{KNOT[2]}" fill="{fill}"/>')
    s = f'stroke="{line}" stroke-linecap="round" stroke-linejoin="round" fill="none"'
    # burger details inside the body, drawn before the inline so they end on it
    seeds = ''.join(f'<ellipse cx="{x}" cy="{y}" rx="11" ry="6.5" fill="{line}" transform="rotate({r} {x} {y})"/>'
                    for x, y, r in [(186, 270, -26), (234, 252, -8), (284, 252, 10), (332, 270, 26), (210, 296, -14), (260, 288, 2), (310, 296, 16)])
    creases = f'<path d="M236 194 Q208 206 180 232 M248 198 Q236 212 226 232 M276 194 Q304 206 332 232 M264 198 Q276 212 286 232" {s} stroke-width="6"/>'
    shine = f'<path d="M136 300 Q140 262 170 238" {s} stroke-width="9"/><path d="M134 430 Q140 450 160 456" {s} stroke-width="7"/>'
    lettuce = f'<path d="{wave(320)}" {s} stroke-width="8"/>'
    drips = (f'<path d="M80 332 L432 332 L432 344 L346 344 C346 344 344 372 334 372 C324 372 322 344 322 344 '
             f'L272 344 C272 344 270 386 256 386 C242 386 240 344 240 344 L192 344 C192 344 190 366 180 366 C170 366 168 344 168 344 L80 344 Z" fill="{cheese}"/>')
    bottom = f'<path d="M80 404 L432 404" {s} stroke-width="8"/>'
    details = f'<g clip-path="url(#{p}bodyc)">{lettuce}{drips}{bottom}{seeds}{creases}{shine}</g>'
    body_inline = inline(BODY, f'{p}bodyc', 9, 6, fill, line)
    ear_inline = inline(EAR_L, f'{p}earl', 7, 5, fill, line) + inline(EAR_R, f'{p}earr', 7, 5, fill, line)
    knot = f'<path d="M240 150 Q256 156 272 150" {s} stroke-width="5"/><path d="M234 172 Q256 180 278 172" {s} stroke-width="5"/>'
    # clip defs used by details must exist before use: put the body clip first
    # outer edge redrawn on top: hides the antialiasing seam where the clip meets the edge
    seal = f'<g fill="none" stroke="{fill}" stroke-width="{ROUND + 6}" stroke-linejoin="round"><path d="{EAR_L}"/><path d="{EAR_R}"/><path d="{BODY}"/></g>'
    return sil + f'<defs><clipPath id="{p}bodyc"><path d="{BODY}"/></clipPath></defs>' + details + body_inline.replace(f'<clipPath id="{p}bodyc"><path d="{BODY}"/></clipPath>', '') + ear_inline + seal + knot

def svg(vb, body, label='Junkbox'):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{label}"><title>{label}</title>{body}</svg>\n'
def write(name, s): open(os.path.join(OUT, name), 'w').write(s); print('wrote', name)

# ---------------- lockups with Junkbox's own hand lettering ----------------
TR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'trace')
WORD = open(os.path.join(TR, 'd-word.txt')).read(); TAG = open(os.path.join(TR, 'd-tag.txt')).read()
WB = (769, 316, 2208, 548); TB = (516, 2644, 2564, 2721)
MB = (82, 54, 430, 498)  # mark bounds on the 512 grid, rounding stroke included
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

stacked('junkbag-round-stacked-on-amber.svg', AMBER, INK)
stacked('junkbag-round-stacked-on-ink.svg', INK, AMBER, fill=AMBER, line=INK, cheese=WHITE)
stacked('junkbag-round-stacked-on-white.svg', None, INK)
horizontal('junkbag-round-horizontal-on-amber.svg', AMBER, INK)
horizontal('junkbag-round-horizontal-on-white.svg', None, INK)
avatar('junkbag-round-avatar.svg')
write('junkbag-round-mark-on-amber.svg', svg('0 0 512 512', f'<rect width="512" height="512" fill="{AMBER}"/>' + mark()))
write('junkbag-round-mark.svg', svg('0 0 512 512', mark()))
write('junkbag-round-mark-on-ink.svg', svg('0 0 512 512', f'<rect width="512" height="512" fill="{INK}"/>' + mark(fill=AMBER, line=INK, cheese=WHITE)))
