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

## Final direction (`junkbag-final-*`)

The minimal burger, **unchanged** (seeds, lettuce, cheese drips, bottom line, white inner contour), with a top that reads clearly as a tied bin bag rather than round ears or a propeller cap:

- a taller **pinched neck** rising from the bag's shoulders, with three white **creases** where the plastic gathers;
- the white **tie band** across the neck and a small knot;
- two **crumpled plastic flaps** with cut, notched ends, asymmetric: the left one tall and upright, the right one shorter and swung out sideways.

Files: `junkbag-final-mark.svg`, `-mark-on-amber.svg`, `-mark-on-ink.svg`, `-stacked-on-amber.svg` (primary), `-stacked-on-ink.svg`, `-stacked-on-white.svg`, `-horizontal-on-amber.svg`, `-horizontal-on-white.svg`, `-avatar.svg`; board: `junk-bag-final-board.png`.

Rebuild: `python3 tools/bag_mark_final.py logo-concepts/junk-bag`

## v5: classic bin bag with the burger inside (`junkbag-v5-*`)

The bag no longer follows the burger. It has its own traditional bin-bag silhouette: a wide, slightly sagging bottom, shoulders tapering to a pinched neck, white tie band and gather creases, a knot, and two big pointed tie ends swept up and out. The minimal burger (unchanged, with its white contour, seeds, lettuce, cheese drips and bottom line) sits at 60% size in the lower half of the bag, with generous black padding around it.

Files: `junkbag-v5-mark.svg`, `-mark-on-amber.svg`, `-mark-on-ink.svg`, `-stacked-on-amber.svg` (primary), `-stacked-on-ink.svg`, `-stacked-on-white.svg`, `-horizontal-on-amber.svg`, `-horizontal-on-white.svg`, `-avatar.svg`; board: `junk-bag-v5-board.png`.

Rebuild: `python3 tools/bag_mark_v5.py logo-concepts/junk-bag`

## v6: bag drawn to the client's reference (`junkbag-v6-*`)

An original drawing in the style of the bag Junkbox sent as a reference (not a trace of it): an egg-shaped body with a flat bottom, a rounded collar at the neck, and a tall gathered top with a peak and one pointed end swept to the right. The collar gaps and the highlights (two in the top, one long one down the right side of the body) are cut out, so they show the background. The minimal burger, unchanged, sits inside at 58% size.

Files: `junkbag-v6-mark.svg`, `-mark-on-amber.svg`, `-mark-on-ink.svg`, `-stacked-on-amber.svg` (primary), `-stacked-on-ink.svg`, `-stacked-on-white.svg`, `-horizontal-on-amber.svg`, `-horizontal-on-white.svg`, `-avatar.svg`; board: `junk-bag-v6-board.png`.

Rebuild: `python3 tools/bag_mark_v6.py logo-concepts/junk-bag`
