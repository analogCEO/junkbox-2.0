import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from glyphs import Face
from fontTools.pens.boundsPen import BoundsPen

FONTS = sys.argv[1]; OUT = sys.argv[2]
os.makedirs(OUT, exist_ok=True)
dela = Face(FONTS + '/fontsource-dela-gothic-one-5.3.0/package/files/*-400-normal.woff2')
mono = Face(FONTS + '/fontsource-martian-mono-5.3.0/package/files/martian-mono-*-500-normal.woff2')

AMBER, INK, PAPER = '#F9B20A', '#16120E', '#FFFBF2'

def ink_bounds(face, text, tracking=0.0):
    """x-extent of inked text at size=upm, and left bearing of first glyph."""
    upm = face.upm; cx = 0; xmin = None; xmax = None
    for ch in text:
        if ch == ' ':
            cx += upm*0.28 + tracking*upm; continue
        ft, g = face.map[ord(ch)]; gs = ft.getGlyphSet()
        bp = BoundsPen(gs); gs[g].draw(bp)
        if bp.bounds:
            a, _, b, _ = bp.bounds
            xmin = cx + a if xmin is None else xmin
            xmax = cx + b
        cx += ft['hmtx'][g][0] + tracking*upm
    return xmin, xmax

def fit(face, text, width, x, baseline, tracking=0.0):
    """Path for text whose ink spans exactly `width`, starting at x."""
    a, b = ink_bounds(face, text, tracking)
    size = width * face.upm / (b - a)
    d, _ = face.text_path(text, x - a*size/face.upm, baseline, size, tracking)
    return d, size

CAP = 0.726  # Dela Gothic cap height / em

def bite_circles(cx, cy, r):
    # three overlapping bites around a corner point (cx, cy): the 'bite' device
    return [(cx - 1.55*r, cy - 0.15*r, r), (cx - 0.55*r, cy + 0.55*r, r), (cx + 0.15*r, cy + 1.55*r, r)]

def mask(id_, w, h, circles):
    c = ''.join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="#000"/>' for x, y, r in circles)
    return f'<mask id="{id_}" maskUnits="userSpaceOnUse" x="0" y="0" width="{w}" height="{h}"><rect width="{w}" height="{h}" fill="#fff"/>{c}</mask>'

def stacked(x, w, top, gap):
    """JUNK over BOX, both lines exactly w wide. Returns paths and total height."""
    d1, s1 = fit(dela, 'JUNK', w, x, 0, -0.02)
    d2, s2 = fit(dela, 'BOX', w, x, 0, -0.02)
    h1, h2 = CAP*s1, CAP*s2
    y1 = top + h1; y2 = y1 + gap + h2
    d1, _ = fit(dela, 'JUNK', w, x, y1, -0.02)
    d2, _ = fit(dela, 'BOX', w, x, y2, -0.02)
    return d1 + d2, h1 + gap + h2

def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{title}">'
            f'<title>{title}</title>{body}</svg>\n')

def write(name, s):
    open(os.path.join(OUT, name), 'w').write(s); print('wrote', name, len(s))

# 1. Box mark — the primary logo. Amber box, bite out of the top-right corner, JUNK/BOX stacked.
S = 512; pad = 52; r = 54
d, th = stacked(pad, S - 2*pad, 0, 22)
top = S - pad - th
d, th = stacked(pad, S - 2*pad, top, 22)
bite = bite_circles(S, 0, r)
write('junkbox-boxmark.svg', svg(S, S,
    mask('bite', S, S, bite) +
    f'<g mask="url(#bite)"><rect width="{S}" height="{S}" rx="20" fill="{AMBER}"/></g>'
    f'<path d="{d}" fill="{INK}"/>', 'Junkbox'))

# 2. Stamp — one ink, letters knocked out. For rubber stamps on kraft boxes and bags.
write('junkbox-stamp.svg', svg(S, S,
    f'<mask id="k" maskUnits="userSpaceOnUse" x="0" y="0" width="{S}" height="{S}"><rect width="{S}" height="{S}" fill="#fff"/>'
    + ''.join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rr:.1f}" fill="#000"/>' for x, y, rr in bite) +
    f'<path d="{d}" fill="#000"/></mask>'
    f'<rect width="{S}" height="{S}" rx="20" fill="{INK}" mask="url(#k)"/>', 'Junkbox'))

# 3. Avatar — circle-safe for Instagram, Glovo, Wolt, TikTok. Bite sits on the circle's edge.
A = 512; ap = 112
d, th = stacked(ap, A - 2*ap, 0, 16)
d, th = stacked(ap, A - 2*ap, (A - th)/2 + 6, 16)
import math
ang = math.radians(-45); ex, ey = A/2 + (A/2)*math.cos(ang), A/2 + (A/2)*math.sin(ang)
bite_a = bite_circles(ex + 10, ey - 10, 40)
write('junkbox-avatar.svg', svg(A, A,
    mask('bite', A, A, bite_a) +
    f'<g mask="url(#bite)"><circle cx="{A/2}" cy="{A/2}" r="{A/2}" fill="{AMBER}"/></g>'
    f'<path d="{d}" fill="{INK}"/>', 'Junkbox'))

# 4. Wordmark — one line, for headers, receipts, tape. Ink on light grounds, amber on ink.
def wordmark(text, fill, name, label, h=120, track=-0.01):
    a, b = ink_bounds(dela, text, track)
    size = h / CAP
    w = (b - a) * size / dela.upm
    padx, pady = 8, 8
    dd, _ = dela.text_path(text, padx - a*size/dela.upm, pady + h, size, track)
    # bite out of the top-right corner of the last letter
    W, H = w + 2*padx, h + 2*pady
    bc = bite_circles(W - padx, pady, h*0.13)
    write(name, svg(round(W), round(H), mask('bite', round(W), round(H), bc) +
        f'<path d="{dd}" fill="{fill}" mask="url(#bite)"/>', label))
wordmark('JUNKBOX', INK, 'junkbox-wordmark-ink.svg', 'Junkbox')
wordmark('JUNKBOX', AMBER, 'junkbox-wordmark-amber.svg', 'Junkbox')
wordmark('ДЖЪНКБОКС', INK, 'junkbox-wordmark-cyrillic-ink.svg', 'Джънкбокс')

# 5. The bite on its own — a graphic device for crops, stickers, dividers.
B = 200
bc = bite_circles(B, 0, 46)
write('bite-device.svg', svg(B, B, mask('bite', B, B, bc) +
    f'<g mask="url(#bite)"><rect width="{B}" height="{B}" fill="{INK}"/></g>', 'Bite device'))
