"""Outline text to SVG path data from a set of (possibly subsetted) font files."""
import glob, sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

class Face:
    def __init__(self, pattern):
        self.map = {}
        self.upm = None
        for f in sorted(glob.glob(pattern)):
            ft = TTFont(f)
            self.upm = self.upm or ft['head'].unitsPerEm
            cmap = ft.getBestCmap() or {}
            for cp, gname in cmap.items():
                self.map.setdefault(cp, (ft, gname))
        self.asc = None

    def has(self, ch): return ord(ch) in self.map

    def advance(self, ch):
        ft, g = self.map[ord(ch)]
        return ft['hmtx'][g][0]

    def text_path(self, text, x, y, size, tracking=0.0):
        """Return (path_d, width). Baseline at y. tracking in em."""
        s = size / self.upm
        pen = SVGPathPen(None)
        cx = 0.0
        for ch in text:
            if ch == ' ':
                cx += self.upm * 0.28 + tracking * self.upm; continue
            ft, g = self.map[ord(ch)]
            gs = ft.getGlyphSet()
            from fontTools.pens.recordingPen import DecomposingRecordingPen
            rp = DecomposingRecordingPen(gs); gs[g].draw(rp)
            rp.replay(TransformPen(pen, (s, 0, 0, -s, x + cx * s, y)))
            cx += ft['hmtx'][g][0] + tracking * self.upm
        width = (cx - tracking * self.upm) * s
        return pen.getCommands(), width

    def bbox_height(self, ch, size):
        ft, g = self.map[ord(ch)]
        from fontTools.pens.boundsPen import BoundsPen
        bp = BoundsPen(ft.getGlyphSet()); ft.getGlyphSet()[g].draw(bp)
        return bp.bounds and (bp.bounds[3] - bp.bounds[1]) * size / self.upm, bp.bounds
