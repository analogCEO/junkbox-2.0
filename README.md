# Junkbox 2.0

Brand refresh and design system for Junkbox, a street-food counter at Пиротска 61, Sofia.

The live, browsable version of the design system is a private claude.ai artifact: https://claude.ai/artifact/6YxiSAYDBLBrfTejMjvhud (share it from the page's Share menu).

## What's here

| Path | Contents |
| --- | --- |
| `design-system/project/README.md` | The brand book: name, logo, colour, type, writing, photography, the bite, packaging. |
| `design-system/project/Audit.md` | What Junkbox publishes today (Glovo, Wolt, Instagram), checked 14 Nov 2026, and the fix for each problem. |
| `design-system/project/Content-ideas.md` | Social series, launch sequence for the new identity, ideas to test. |
| `design-system/project/tokens.json` | Colour (light and dark), type, spacing, radius and shadow tokens. `tokens.css` is generated from it. |
| `design-system/project/components/` | Eight components with live previews and guidelines: Logo, Button, Tag, HeatMeter, PriceTag, MenuCard, SocialPost, BagSeal. Styles in `bundle.css`. |
| `design-system/project/assets/Logos/` | The new marks as outlined SVGs: box mark, avatar, stamp, wordmarks (Latin and Cyrillic), the bite. |
| `research/` | The Glovo menu as scraped on 14 Nov 2026, the annotated photo audit, the current logo and Glovo cover. |
| `tools/` | Scripts that rebuild the logos from Dela Gothic One and `tokens.css` from `tokens.json`. |

## Rebuilding

```sh
# logos (needs fonttools + brotli, and the @fontsource packages unpacked into <fonts-dir>)
pip install fonttools brotli
npm pack @fontsource/dela-gothic-one @fontsource/martian-mono   # unpack each .tgz into <fonts-dir>/<name>/
python3 tools/make_logos.py <fonts-dir> design-system/project/assets/Logos

# tokens.css after editing tokens.json
python3 tools/build_tokens_css.py
```

Fonts: Dela Gothic One, Onest and Martian Mono, all from Google Fonts under the SIL Open Font License, all with Cyrillic.
