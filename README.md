# Junkbox 2.0

Brand refresh and design system for Junkbox, a street-food counter at Пиротска 61, Sofia.

The live, browsable version of the design system is a private claude.ai artifact: https://claude.ai/artifact/6YxiSAYDBLBrfTejMjvhud (share it from the page's Share menu).

## What's here

| Path | Contents |
| --- | --- |
| `design-system/project/README.md` | The brand book, built around the existing Junkbox logo: name, logo use, colour, type, writing, photography, packaging. |
| `design-system/project/Audit.md` | What Junkbox publishes today (Glovo, Wolt, Instagram), checked 14 Nov 2026, and the fix for each problem. |
| `design-system/project/Content-ideas.md` | Social series, launch sequence for the new identity, ideas to test. |
| `design-system/project/tokens.json` | Colour (light and dark), type, spacing, radius and shadow tokens. `tokens.css` is generated from it. |
| `design-system/project/components/` | Seven components with live previews and guidelines: Logo, Button, Tag, PriceTag, MenuCard, SocialPost, BagSeal. Styles in `bundle.css`. |
| `design-system/project/assets/Logos/` | Junkbox's own logo traced to vector, in every lockup: primary (ink, white), amber and ink tiles, avatar, icon, wordmarks, horizontal. Plus the two original PNGs. |
| `research/` | The Glovo menu as scraped on 14 Nov 2026, the annotated photo audit, the current logo and Glovo cover. |
| `tools/` | Scripts that rebuild the logo set from the traced artwork (`tools/trace/`) and `tokens.css` from `tokens.json`. |

## Rebuilding

```sh
# logo set, from the traced paths in tools/trace (traced from the supplied 750px PNG, upscaled 4x, with potrace)
python3 tools/make_logo_set.py tools/trace design-system/project/assets/Logos

# tokens.css after editing tokens.json
python3 tools/build_tokens_css.py
```

Fonts: Neucha (headlines, a stand-in for the logo's hand lettering) and Montserrat (everything else), both from Google Fonts under the SIL Open Font License, both with Cyrillic.
