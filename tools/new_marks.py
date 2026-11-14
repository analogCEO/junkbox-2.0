"""Concept marks for a new Junkbox logo: stylised bin + burger, and trash bag + burger.

Flat, thick ink outline, two fills (amber + white), so each reads at 48 px and prints in one ink.
Usage: python3 new_marks.py <out dir>
"""
import math, os, sys
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
INK, AMBER, WHITE = '#231F20', '#F7AF0B', '#FFFFFF'
SW = 16  # outline weight on the 512 grid

def st(fill, w=SW):
    return f'fill="{fill}" stroke="{INK}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"'

def seeds(pts, rot=-20):
    return ''.join(f'<ellipse cx="{x}" cy="{y}" rx="9" ry="5" fill="{WHITE}" stroke="{INK}" stroke-width="5" transform="rotate({rot + (i % 3 - 1) * 25} {x} {y})"/>' for i, (x, y) in enumerate(pts))

def ribs(xs, y0, y1, cx=256, k=0.86, w=12):
    return ''.join(f'<line x1="{x}" y1="{y0}" x2="{cx + (x - cx) * k:.1f}" y2="{y1}" stroke="{INK}" stroke-width="{w}" stroke-linecap="round"/>' for x in xs)

def svg(body, vb='0 0 512 512', label='Junkbox'):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{label}"><title>{label}</title>{body}</svg>\n'

# ---------------- A. Burger Bin: the lid is the top bun ----------------
def burger_bin():
    handles = (f'<path d="M154 340 L124 340 Q114 340 114 350 L114 368 Q114 378 124 378 L150 378" {st(WHITE)}/>'
               f'<path d="M358 340 L388 340 Q398 340 398 350 L398 368 Q398 378 388 378 L362 378" {st(WHITE)}/>')
    can = handles + f'<path d="M150 304 L362 304 L348 448 L164 448 Z" {st(WHITE)}/>' + f'<rect x="156" y="446" width="200" height="30" rx="10" {st(WHITE)}/>'
    rib = ribs([200, 228, 256, 284, 312], 330, 428, k=0.9)
    patty = f'<path d="M146 262 Q146 240 168 240 L344 240 Q366 240 366 262 L366 270 Q366 292 344 292 L168 292 Q146 292 146 270 Z" fill="{INK}"/>'
    rim = f'<rect x="130" y="286" width="252" height="30" rx="15" {st(WHITE)}/>'
    cheese = f'<path d="M136 226 L376 226 L376 244 L354 244 L342 288 L330 244 L270 244 L256 300 L242 244 L190 244 L176 280 L162 244 L136 244 Z" {st(AMBER, 12)}/>'
    lettuce = f'<path d="M124 214 Q140 196 156 214 Q172 196 188 214 Q204 196 220 214 Q236 196 252 214 Q268 196 284 214 Q300 196 316 214 Q332 196 348 214 Q364 196 380 214 Q392 226 380 234 L132 234 Q118 226 124 214 Z" {st(WHITE, 12)}/>'
    bun = (f'<g transform="rotate(-7 256 214)">'
           f'<path d="M226 104 Q226 74 256 74 Q286 74 286 104" fill="none" stroke="{INK}" stroke-width="{SW}" stroke-linecap="round"/>'
           f'<path d="M116 206 C116 138 182 100 256 100 C330 100 396 138 396 206 Q396 218 384 218 L128 218 Q116 218 116 206 Z" {st(AMBER)}/>'
           + seeds([(184, 150), (228, 128), (276, 126), (322, 146), (206, 182), (256, 168), (304, 180), (348, 182)]) +
           '</g>')
    motion = f'<path d="M404 118 Q420 132 418 152 M426 96 Q450 116 448 146" fill="none" stroke="{INK}" stroke-width="10" stroke-linecap="round"/>'
    return can + rib + patty + rim + cheese + lettuce + bun + motion

# ---------------- B. Overflow: bin with the lid popped by burger, fries and cola ----------------
def overflow():
    can = f'<path d="M156 300 L356 300 L342 460 Q340 480 320 480 L192 480 Q172 480 170 460 Z" {st(WHITE)}/>'
    rib = ribs([204, 230, 256, 282, 308], 326, 454)
    fries = ''.join(f'<rect x="{x}" y="{y}" width="22" height="120" rx="6" {st(AMBER, 10)} transform="rotate({r} {x+11} {y+120})"/>' for x, y, r in [(132, 168, -24), (152, 150, -14), (174, 160, -4)])
    cup = (f'<g transform="rotate(16 356 300)"><path d="M318 160 L398 160 L388 300 L328 300 Z" {st(WHITE, 12)}/>'
           f'<rect x="312" y="146" width="92" height="22" rx="8" {st(WHITE, 12)}/>'
           f'<path d="M366 146 L380 92 L404 86" fill="none" stroke="{INK}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>'
           f'<path d="M332 210 L384 210" stroke="{INK}" stroke-width="10" stroke-linecap="round"/></g>')
    bottom_bun = f'<rect x="170" y="252" width="172" height="34" rx="17" {st(AMBER, 12)}/>'
    patty = f'<rect x="162" y="222" width="188" height="36" rx="18" fill="{INK}"/>'
    cheese = f'<path d="M164 214 L348 214 L348 228 L330 228 L320 258 L310 228 L262 228 L252 266 L242 228 L196 228 L186 252 L176 228 L164 228 Z" {st(AMBER, 10)}/>'
    top_bun = (f'<path d="M166 210 C166 150 210 126 256 126 C302 126 346 150 346 210 Z" {st(AMBER, 12)}/>'
               + seeds([(214, 162), (256, 146), (298, 162), (236, 186), (278, 186)]))
    rim = f'<rect x="138" y="284" width="236" height="28" rx="14" {st(WHITE)}/>'
    lid = (f'<g transform="rotate(-18 256 100)"><path d="M150 112 Q150 96 166 96 L346 96 Q362 96 362 112 Z" {st(WHITE)}/>'
           f'<path d="M232 96 Q232 70 256 70 Q280 70 280 96" fill="none" stroke="{INK}" stroke-width="{SW}" stroke-linecap="round"/></g>')
    motion = f'<path d="M108 120 Q96 136 100 156 M84 104 Q66 126 72 152" fill="none" stroke="{INK}" stroke-width="10" stroke-linecap="round"/>'
    return fries + cup + can + rib + bottom_bun + patty + cheese + top_bun + rim + lid + motion

# ---------------- C. Junk Bag: a black bin bag, tied, with a burger bursting through a tear ----------------
def junk_bag():
    body = 'M214 156 C156 178 100 250 100 344 C100 436 166 484 256 484 C346 484 412 436 412 344 C412 250 356 178 298 156 Z'
    bag = f'<path d="{body}" {st(INK)}/>'
    neck = f'<path d="M216 158 Q256 172 296 158 L282 122 Q256 132 230 122 Z" {st(INK)}/>'
    ears = (f'<path d="M234 124 C206 88 162 98 146 70 C196 60 236 86 250 120 Z" {st(INK)}/>'
            f'<path d="M278 124 C306 88 350 98 366 70 C316 60 276 86 262 120 Z" {st(INK)}/>')
    shine = (f'<path d="M150 262 Q136 300 140 344 M168 232 Q162 242 158 252 M236 146 Q244 140 254 142" fill="none" stroke="{WHITE}" stroke-width="10" stroke-linecap="round"/>'
             f'<path d="M226 120 Q256 130 286 120" fill="none" stroke="{WHITE}" stroke-width="7" stroke-linecap="round"/>'
             f'<path d="M168 92 Q196 92 222 110 M344 92 Q316 92 290 110" fill="none" stroke="{WHITE}" stroke-width="6" stroke-linecap="round"/>')
    tear = 'M132 296 L164 250 L186 270 L222 232 L246 258 L282 228 L304 256 L340 240 L352 268 L384 280 L374 330 L392 372 L362 396 L366 444 L320 432 L286 462 L256 438 L218 460 L198 432 L152 440 L156 398 L124 372 L144 334 Z'
    clip = f'<clipPath id="tear"><path d="{tear}"/></clipPath>'
    burger = (f'<g clip-path="url(#tear)"><rect x="100" y="230" width="312" height="230" fill="{AMBER}"/>'
              f'<path d="M136 322 C136 262 196 236 256 236 C316 236 376 262 376 322 Z" fill="{AMBER}" stroke="{INK}" stroke-width="12"/>'
              + seeds([(196, 282), (240, 262), (286, 262), (330, 282), (218, 302), (264, 290), (310, 304)]) +
              f'<path d="M136 330 Q152 314 168 330 Q184 314 200 330 Q216 314 232 330 Q248 314 264 330 Q280 314 296 330 Q312 314 328 330 Q344 314 360 330 Q376 314 380 330 L380 344 L136 344 Z" fill="{WHITE}" stroke="{INK}" stroke-width="10" stroke-linejoin="round"/>'
              f'<rect x="132" y="344" width="252" height="40" rx="20" fill="{INK}"/>'
              f'<path d="M136 346 L380 346 L380 358 L350 358 L338 388 L326 358 L272 358 L260 396 L248 358 L196 358 L184 384 L172 358 L136 358 Z" fill="{AMBER}" stroke="{INK}" stroke-width="8" stroke-linejoin="round"/>'
              f'<path d="M136 392 L380 392 L380 414 Q380 450 344 450 L172 450 Q136 450 136 414 Z" fill="{AMBER}" stroke="{INK}" stroke-width="12"/></g>')
    edge = f'<path d="{tear}" fill="none" stroke="{WHITE}" stroke-width="18" stroke-linejoin="round"/><path d="{tear}" fill="none" stroke="{INK}" stroke-width="7" stroke-linejoin="round"/>'
    return f'<defs>{clip}</defs>' + bag + neck + ears + shine + burger + edge

marks = {'concept-a-burger-bin': burger_bin(), 'concept-b-overflow': overflow(), 'concept-c-junk-bag': junk_bag()}
import re
for name, body in marks.items():
    open(os.path.join(OUT, name + '.svg'), 'w').write(svg(body)); print('wrote', name)
    # Sticker: the same drawing over a white die-cut outline, so it holds on ink and on photos.
    halo = body.replace(f'stroke="{INK}"', 'stroke="#FFFFFF"').replace(f'fill="{INK}"', 'fill="#FFFFFF"').replace(f'fill="{AMBER}"', 'fill="#FFFFFF"')
    halo = halo.replace('id="tear"', 'id="tear-h"').replace('url(#tear)', 'url(#tear-h)')
    halo = re.sub(r'stroke-width="(\d+)"', lambda m: f'stroke-width="{int(m.group(1)) + 30}"', halo)
    open(os.path.join(OUT, name + '-sticker.svg'), 'w').write(svg(f'<g>{halo}</g>' + body, vb='-24 -24 560 560'))

# ---------------- Lockups with Junkbox's own hand lettering (traced, tools/trace) ----------------
TR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'trace')
WORD = open(os.path.join(TR, 'd-word.txt')).read(); TAG = open(os.path.join(TR, 'd-tag.txt')).read()
WB = (769, 316, 2208, 548); TB = (516, 2644, 2564, 2721)  # bounds in the 3000 grid
def placed(d, b, x, y, w, fill=INK):
    k = w / (b[2] - b[0])
    return f'<path fill-rule="evenodd" fill="{fill}" transform="translate({x - b[0]*k:.2f} {y - b[1]*k:.2f}) scale({k:.5f})" d="{d}"/>', (b[3] - b[1]) * k
for name, body in marks.items():
    # stacked: mark over JUNKBOX over CAFE & FAST FOOD, 600 wide
    w_word, w_tag = 440, 470
    word, hw = placed(WORD, WB, (600 - w_word) / 2, 520, w_word)
    tag, ht = placed(TAG, TB, (600 - w_tag) / 2, 520 + hw + 34, w_tag)
    H = 520 + hw + 34 + ht + 30
    open(os.path.join(OUT, name + '-stacked.svg'), 'w').write(svg(f'<g transform="translate(64 0)">{body}</g>' + word + tag, vb=f'0 0 640 {H:.0f}'))
    # horizontal: mark left, lettering right
    word, hw = placed(WORD, WB, 540, 200, 560)
    tag, ht = placed(TAG, TB, 540, 200 + hw + 36, 560)
    open(os.path.join(OUT, name + '-horizontal.svg'), 'w').write(svg(body + word + tag, vb='0 0 1130 512'))
