"""Build the Junkbox logo set from the traced artwork (paths traced from the client's own 750px PNG, upscaled 4x).

Usage: python3 make_logo_set.py <dir with d-word.txt d-illo.txt d-tag.txt> <out dir>
Coordinates are the 3000 x 3000 space of the original file x4.
"""
import os, sys
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
D = {n: open(os.path.join(src, f'd-{n}.txt')).read() for n in ('word', 'illo', 'tag')}
B = {'word': (769, 316, 2208, 548), 'illo': (688, 718, 2342, 2511), 'tag': (516, 2644, 2564, 2721)}
INK, AMBER, WHITE = '#231F20', '#F7AF0B', '#FFFFFF'

def w(n): return B[n][2] - B[n][0]
def h(n): return B[n][3] - B[n][1]
def part(n, fill, X=None, Y=None, s=1.0):
    if X is None:
        return f'<path fill-rule="evenodd" fill="{fill}" d="{D[n]}"/>'
    tx, ty = X - B[n][0] * s, Y - B[n][1] * s
    return f'<path fill-rule="evenodd" fill="{fill}" transform="translate({tx:.2f} {ty:.2f}) scale({s:.5f})" d="{D[n]}"/>'
def svg(vb, body, label='Junkbox'):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{label}"><title>{label}</title>{body}</svg>\n'
def write(name, s):
    open(os.path.join(out, name), 'w').write(s); print(f'{name:38s} {len(s)//1024} KB')

PAD = 90
# 1-2. Primary: the logo exactly as drawn — wordmark, illustration, tagline.
x0, y0, x1, y1 = 516 - PAD, 316 - PAD, 2564 + PAD, 2721 + PAD
vb = f'{x0} {y0} {x1-x0} {y1-y0}'
for name, fill in (('junkbox-logo-ink.svg', INK), ('junkbox-logo-white.svg', WHITE)):
    write(name, svg(vb, part('word', fill) + part('illo', fill) + part('tag', fill)))

# 3-4. Square tiles, the layout of the client's amber file (no tagline).
write('junkbox-tile-amber.svg', svg('0 0 3000 3000', f'<rect width="3000" height="3000" fill="{AMBER}"/>' + part('word', INK) + part('illo', INK)))
write('junkbox-tile-ink.svg', svg('0 0 3000 3000', f'<rect width="3000" height="3000" fill="{INK}"/>' + part('word', AMBER) + part('illo', AMBER)))

# 5. Avatar: amber square, illustration only, sized to sit inside the circle crop of Instagram, TikTok, Glovo.
s = 1950 / h('illo')
X = (3000 - w('illo') * s) / 2; Y = (3000 - h('illo') * s) / 2 + 40
write('junkbox-avatar.svg', svg('0 0 3000 3000', f'<rect width="3000" height="3000" fill="{AMBER}"/>' + part('illo', INK, X, Y, s)))

# 6. Icon: the illustration alone, transparent.
x0, y0, x1, y1 = 688 - PAD, 718 - PAD, 2342 + PAD, 2511 + PAD
write('junkbox-icon-ink.svg', svg(f'{x0} {y0} {x1-x0} {y1-y0}', part('illo', INK)))

# 7. Wordmark alone.
x0, y0, x1, y1 = 769 - PAD, 316 - PAD, 2208 + PAD, 548 + PAD
for name, fill in (('junkbox-wordmark-ink.svg', INK), ('junkbox-wordmark-white.svg', WHITE)):
    write(name, svg(f'{x0} {y0} {x1-x0} {y1-y0}', part('word', fill)))

# 8. Wordmark over tagline, no illustration: receipts, tape, narrow strips.
st = w('word') / w('tag'); gap = 120
body = part('word', INK, 0, 0, 1) + part('tag', INK, 0, h('word') + gap, st)
H = h('word') + gap + h('tag') * st
write('junkbox-wordmark-tagline-ink.svg', svg(f'{-PAD} {-PAD} {w("word")+2*PAD} {H+2*PAD:.0f}', body))

# 9. Horizontal lockup (proposal): illustration left, wordmark and tagline right.
sw = 2.0; TW = w('word') * sw; st = TW / w('tag'); gap = 170
TH = h('word') * sw + gap + h('tag') * st
IH = h('illo'); tx = w('illo') + 220; ty = (IH - TH) / 2
body = part('illo', INK, 0, 0, 1) + part('word', INK, tx, ty, sw) + part('tag', INK, tx, ty + h('word') * sw + gap, st)
write('junkbox-horizontal-ink.svg', svg(f'{-PAD} {-PAD} {tx+TW+2*PAD:.0f} {IH+2*PAD}', body))
