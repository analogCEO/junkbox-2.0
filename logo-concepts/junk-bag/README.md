# Junk Bag: negative-space mark

One ink silhouette on amber that reads two ways:

- **The outline is a tied bin bag:** twisted neck, two plastic tie ends, gathered creases fanning from the knot, a slightly saggy body and a lumpy bottom.
- **The negative space is a burger:** sesame seeds on the dome (top bun), a wavy gap (lettuce), cheese drips into the patty, and a gap above the bottom bun. The shine on the dome works as both plastic sheen and glossy brioche.

Paired with Junkbox's own hand-lettered JUNKBOX and CAFE & FAST FOOD (traced from the supplied logo).

| File | Use |
| --- | --- |
| `junkbag-mark-on-amber.svg` | The mark on its amber square. |
| `junkbag-mark-ink.svg` | Ink mark, transparent cut-outs: white or light grounds, one-colour stamps and prints. |
| `junkbag-mark-amber-on-ink.svg` | Amber mark on ink. |
| `junkbag-stacked-on-amber.svg` | Primary lockup: mark, wordmark, tagline on amber. |
| `junkbag-stacked-amber-on-ink.svg`, `junkbag-stacked-ink.svg` | The same on ink, and on white/transparent. |
| `junkbag-horizontal-on-amber.svg`, `junkbag-horizontal-ink.svg` | Horizontal lockup for headers, fascia, receipts. |
| `junkbag-avatar.svg` | Profile picture: mark centred on amber, safe for round crops. |

Rebuild: `python3 tools/bag_mark.py logo-concepts/junk-bag`

## Rounded version (`junkbag-round-*`)

Softer shapes and a white inner contour: a rounder bag with a round bottom, rounded tie ears and knot, rounded cheese drips, and a white line running just inside the edge of the bag and the ears. The burger inside is drawn in white lines (seeds, lettuce, the line above the bottom bun, creases, shine) with amber cheese. On ink, the colours swap: amber bag, ink lines, white cheese.

Files: `junkbag-round-mark.svg`, `-mark-on-amber.svg`, `-mark-on-ink.svg`, `-stacked-on-amber.svg` (primary), `-stacked-on-ink.svg`, `-stacked-on-white.svg`, `-horizontal-on-amber.svg`, `-horizontal-on-white.svg`, `-avatar.svg`; board: `junk-bag-round-board.png`.

Rebuild: `python3 tools/bag_mark_round.py logo-concepts/junk-bag`

## Minimal version (`junkbag-min-*`) — current favourite

The rounded version stripped to what carries the idea, with everything thicker:

- **Kept:** the bag silhouette, two round tie ears and the knot, a white tie band on the neck, the white inner contour (now 11 px on the 512 grid), three large sesame seeds, a bold lettuce wave with fewer waves, three big rounded cheese drips, and the line above the bottom bun.
- **Removed:** the creases under the knot, the twist lines, both shine marks, the contour inside the ears, and four of the seven seeds.

Files: `junkbag-min-mark.svg`, `-mark-on-amber.svg`, `-mark-on-ink.svg`, `-stacked-on-amber.svg` (primary), `-stacked-on-ink.svg`, `-stacked-on-white.svg`, `-horizontal-on-amber.svg`, `-horizontal-on-white.svg`, `-avatar.svg`; board: `junk-bag-min-board.png`.

Rebuild: `python3 tools/bag_mark_min.py logo-concepts/junk-bag`
