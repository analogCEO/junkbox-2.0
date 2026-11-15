"""Export the v8 sticker logo as a layered SVG for manual finishing in Illustrator.
No masks: gaps and pleats are white strokes on top. Inlines use simple clipping masks. Strokes stay live.
Usage: python3 export_illustrator.py <out dir>
"""
import os, sys, tempfile
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
sys.argv[1] = tempfile.mkdtemp()
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bag_mark_v8 as v
INK, AMBER, WHITE = v.INK, v.AMBER, v.WHITE
rl = 'stroke-linecap="round" stroke-linejoin="round"'

def burger():
    s = f'fill="none" stroke="{WHITE}" {rl}'
    seeds = ''.join(f'<ellipse cx="{x}" cy="{y}" rx="17" ry="10" fill="{WHITE}" transform="rotate({r} {x} {y})"/>' for x, y, r in [(198, 268, -18), (258, 252, 0), (318, 268, 18)])
    drips = ('M80 336 L432 336 L432 352 L350 352 C350 352 350 384 334 384 C318 384 318 352 318 352 L276 352 C276 352 276 402 256 402 '
             'C236 402 236 352 236 352 L196 352 C196 352 196 380 182 380 C168 380 168 352 168 352 L80 352 Z')
    return (f'<g id="Burger" transform="translate({v.CX - 256*v.K:.1f} {v.CY - 330*v.K:.1f}) scale({v.K})">'
            f'<clipPath id="burger-clip"><path d="{v.BURGER}"/></clipPath>'
            f'<g id="Burger-inside" clip-path="url(#burger-clip)">'
            f'<path id="Lettuce" d="{v.wave(318)}" {s} stroke-width="14"/>'
            f'<path id="Cheese" d="{drips}" fill="{AMBER}"/>'
            f'<path id="Bottom-bun-line" d="M80 418 L432 418" {s} stroke-width="14"/>'
            f'<g id="Seeds">{seeds}</g>'
            f'<path id="Burger-contour-white" d="{v.BURGER}" fill="none" stroke="{WHITE}" stroke-width="76"/>'
            f'<path id="Burger-contour-black-edge" d="{v.BURGER}" fill="none" stroke="{INK}" stroke-width="26"/></g>'
            f'<path id="Burger-outer-edge" d="{v.BURGER}" fill="none" stroke="{INK}" stroke-width="10"/></g>')

def mark():
    w = f'fill="none" stroke="{WHITE}" {rl}'
    return ('<g id="Mark">'
            f'<g id="Sticker-white" fill="{WHITE}" stroke="{WHITE}" stroke-width="58" {rl}><path d="{v.TOP}"/><path d="{v.COLLAR}"/><path d="{v.BODY}"/></g>'
            f'<path id="Bag-body" d="{v.BODY}" fill="{INK}" stroke="{INK}" stroke-width="10" stroke-linejoin="round"/>'
            f'<path id="Bag-collar" d="{v.COLLAR}" fill="{INK}" stroke="{INK}" stroke-width="10" stroke-linejoin="round"/>'
            f'<path id="Bag-top" d="{v.TOP}" fill="{INK}" stroke="{INK}" stroke-width="18" stroke-linejoin="round"/>'
            '<g id="Gaps-and-pleats">'
            f'<path id="Gap-collar-body" d="M210 202 Q256 214 302 202" {w} stroke-width="9"/>'
            f'<path id="Gap-top-collar" d="M220 168 Q256 157 292 168" {w} stroke-width="8"/>'
            f'<path id="Pleat-left" d="M244 154 Q234 124 218 96" {w} stroke-width="8"/>'
            f'<path id="Pleat-centre" d="M256 152 L256 112" {w} stroke-width="8"/>'
            f'<path id="Pleat-right" d="M268 154 Q280 128 294 98" {w} stroke-width="8"/></g>'
            f'<clipPath id="bag-clip"><path d="{v.BODY}"/></clipPath>'
            '<g id="Bag-inline" clip-path="url(#bag-clip)">'
            f'<path id="Bag-inline-white" d="{v.BODY}" fill="none" stroke="{WHITE}" stroke-width="46"/>'
            f'<path id="Bag-inline-black-edge" d="{v.BODY}" fill="none" stroke="{INK}" stroke-width="28"/></g>'
            f'<path id="Bag-body-outer-edge" d="{v.BODY}" fill="none" stroke="{INK}" stroke-width="10" stroke-linejoin="round"/>'
            + burger() + '</g>')

word, hw = v.placed(v.WORD, v.WB, 56, 620, 400, INK)
tag, _ = v.placed(v.TAG, v.TB, 41, 620 + hw + 30, 430, INK)
word = word.replace('<path ', '<path id="Wordmark-JUNKBOX" ', 1); tag = tag.replace('<path ', '<path id="Tagline" ', 1)
for name, bg in (('junkbox-sticker-logo-editable.svg', AMBER), ('junkbox-sticker-logo-editable-no-background.svg', None)):
    rect = f'<rect id="Background-amber" x="-64" y="-40" width="640" height="800" fill="{bg}"/>' if bg else ''
    open(os.path.join(out, name), 'w').write(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-64 -40 640 800" width="640" height="800">{rect}{mark()}<g id="Lettering">{word}{tag}</g></svg>\n')
    print('wrote', name)
