"""Junk Bag mark: one ink silhouette on amber that reads as a tied bin bag (outline)
and as a burger (negative space: seeds, lettuce, cheese drips, bun gaps).

Usage: python3 bag_mark.py <out dir>
"""
import os, sys, math
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
INK, AMBER = '#231F20', '#F7AF0B'

# ---- the silhouette (positive): knot + ears + bag body whose top is a bun dome ----
EARS = ('M244 132 C232 104 206 76 168 58 C176 92 196 120 226 140 C232 144 238 148 244 150 Z '
        'M268 132 C280 104 306 76 344 58 C336 92 316 120 286 140 C280 144 274 148 268 150 Z')
KNOT = 'M234 150 C232 132 244 120 256 120 C268 120 280 132 278 150 L288 176 L224 176 Z'
BODY = ('M226 172 C190 178 126 202 108 264 C100 292 98 312 100 334 '
        'C98 372 104 400 102 436 C100 466 126 482 160 478 C196 474 220 484 256 480 C292 484 316 474 352 478 '
        'C386 482 412 466 410 436 C408 400 414 372 412 334 C414 312 412 292 404 264 C386 202 322 178 286 172 Z')

def wave(y, x0=60, x1=452, amp=9, period=36, thick=18):
    """A wavy stripe of constant thickness (the lettuce)."""
    n = int((x1 - x0) / (period / 2))
    top = f'M{x0} {y}'
    for i in range(n):
        xa = x0 + (i + 0.5) * period / 2; xb = x0 + (i + 1) * period / 2
        top += f' Q{xa:.1f} {y + (amp if i % 2 else -amp)} {xb:.1f} {y}'
    bot = f' L{x1} {y + thick}'
    for i in reversed(range(n)):
        xa = x0 + (i + 0.5) * period / 2; xb = x0 + i * period / 2
        bot += f' Q{xa:.1f} {y + thick + (amp if i % 2 else -amp)} {xb:.1f} {y + thick}'
    return top + bot + ' Z'

def cuts():
    c = []
    # sesame seeds on the dome
    for x, y, r in [(190, 272, -24), (238, 254, -8), (288, 256, 10), (334, 276, 26), (214, 300, -14), (264, 290, 2), (314, 302, 18)]:
        c.append(f'<ellipse cx="{x}" cy="{y}" rx="12" ry="6.5" transform="rotate({r} {x} {y})"/>')
    # gathered creases fanning out from the knot (the bag cue)
    c.append('<path d="M234 186 Q206 198 176 226 M244 190 Q228 206 216 230 M256 192 L256 222 M268 190 Q284 206 296 230 M278 186 Q306 198 336 226" fill="none" stroke="#000" stroke-width="6.5" stroke-linecap="round"/>')
    # twist rings on the neck
    c.append('<path d="M236 146 Q256 152 276 146 M232 162 Q256 170 280 162" fill="none" stroke="#000" stroke-width="6" stroke-linecap="round"/>')
    # shine: plastic sheen on the bag, gloss on the brioche
    c.append('<path d="M134 290 Q140 254 168 230" fill="none" stroke="#000" stroke-width="10" stroke-linecap="round"/>')
    c.append('<path d="M128 438 Q132 456 150 460" fill="none" stroke="#000" stroke-width="8" stroke-linecap="round"/>')
    # lettuce gap
    c.append(f'<path d="{wave(318)}"/>')
    # cheese drips from the lettuce gap into the patty
    c.append('<path d="M150 336 L170 336 L160 366 Z M236 336 L262 336 L249 378 Z M330 336 L352 336 L341 362 Z"/>')
    # gap between patty and bottom bun
    c.append('<rect x="60" y="392" width="392" height="16" rx="8"/>')
    return ''.join(c)

def mark(fill, cut_id='cut'):
    mask = (f'<mask id="{cut_id}" maskUnits="userSpaceOnUse" x="0" y="0" width="512" height="512">'
            f'<rect width="512" height="512" fill="#fff"/><g fill="#000">{cuts()}</g></mask>')
    return mask, f'<g mask="url(#{cut_id})" fill="{fill}"><path d="{EARS}"/><path d="{KNOT}"/><path d="{BODY}"/></g>'

def svg(vb, body, label='Junkbox'):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{label}"><title>{label}</title>{body}</svg>\n'

def write(name, s): open(os.path.join(OUT, name), 'w').write(s); print('wrote', name)

m, g = mark(INK)
write('junkbag-mark-ink.svg', svg('0 0 512 512', f'<defs>{m}</defs>{g}'))
write('junkbag-mark-on-amber.svg', svg('0 0 512 512', f'<defs>{m}</defs><rect width="512" height="512" fill="{AMBER}"/>{g}'))
m2, g2 = mark(AMBER)
write('junkbag-mark-amber-on-ink.svg', svg('0 0 512 512', f'<defs>{m2}</defs><rect width="512" height="512" fill="{INK}"/>{g2}'))

# ---------------- Lockups with Junkbox's own hand lettering (traced, tools/trace) ----------------
TR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'trace')
WORD = open(os.path.join(TR, 'd-word.txt')).read(); TAG = open(os.path.join(TR, 'd-tag.txt')).read()
WB = (769, 316, 2208, 548); TB = (516, 2644, 2564, 2721)
MB = (98, 58, 414, 484)  # ink bounds of the mark on the 512 grid

def placed(d, b, x, y, w, fill):
    k = w / (b[2] - b[0])
    return f'<path fill-rule="evenodd" fill="{fill}" transform="translate({x - b[0]*k:.2f} {y - b[1]*k:.2f}) scale({k:.5f})" d="{d}"/>', (b[3] - b[1]) * k

def mark_at(x, y, h, fill, cid):
    m, g = mark(fill, cid)
    k = h / (MB[3] - MB[1])
    return m, f'<g transform="translate({x - MB[0]*k:.2f} {y - MB[1]*k:.2f}) scale({k:.4f})">{g}</g>', (MB[2] - MB[0]) * k

def stacked(fg, bg, name):
    W = 1000; pad = 110
    m, g, mw = mark_at(0, pad, 470, fg, 'c1')
    g = f'<g transform="translate({(W - mw)/2:.1f} 0)">{g}</g>'
    word, hw = placed(WORD, WB, (W - 560) / 2, pad + 470 + 70, 560, fg)
    tag, ht = placed(TAG, TB, (W - 600) / 2, pad + 470 + 70 + hw + 40, 600, fg)
    H = pad + 470 + 70 + hw + 40 + ht + pad
    rect = f'<rect width="{W}" height="{H:.0f}" fill="{bg}"/>' if bg else ''
    write(name, svg(f'0 0 {W} {H:.0f}', f'<defs>{m}</defs>{rect}{g}{word}{tag}'))

def horizontal(fg, bg, name):
    pad = 60; mh = 300
    m, g, mw = mark_at(pad, pad, mh, fg, 'c2')
    tx = pad + mw + 56
    word, hw = placed(WORD, WB, tx, pad + 92, 560, fg)
    tag, ht = placed(TAG, TB, tx, pad + 92 + hw + 34, 560, fg)
    W, H = tx + 560 + pad, mh + 2 * pad
    rect = f'<rect width="{W:.0f}" height="{H}" fill="{bg}"/>' if bg else ''
    write(name, svg(f'0 0 {W:.0f} {H}', f'<defs>{m}</defs>{rect}{g}{word}{tag}'))

def avatar(name):
    m, g, mw = mark_at(0, 0, 330, INK, 'c3')
    g = f'<g transform="translate({(512 - mw)/2:.1f} {(512 - 330)/2 + 4:.1f})">{g}</g>'
    write(name, svg('0 0 512 512', f'<defs>{m}</defs><rect width="512" height="512" fill="{AMBER}"/>{g}'))

stacked(INK, AMBER, 'junkbag-stacked-on-amber.svg')
stacked(AMBER, INK, 'junkbag-stacked-amber-on-ink.svg')
stacked(INK, None, 'junkbag-stacked-ink.svg')
horizontal(INK, AMBER, 'junkbag-horizontal-on-amber.svg')
horizontal(INK, None, 'junkbag-horizontal-ink.svg')
avatar('junkbag-avatar.svg')
