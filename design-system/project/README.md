Junkbox is a cafe and fast-food counter at Пиротска 61, Sofia: brioche burgers, tortillas, quesadillas, fried boxes and breakfast, sold over the counter and through Glovo. The identity is the logo Junkbox already has: a hand-drawn trash can overflowing with a burger, fries, cola and pizza, hand-lettered JUNKBOX, the tagline CAFE & FAST FOOD, in ink on white or on amber. This system keeps that logo as drawn and makes everything around it consistent.

## The look in one line

**Ink drawing on amber.** Black hand-drawn line work, hand lettering and wide-tracked caps, on the logo's amber or on white. Nothing glossy, no gradients, no stock photos.

## Name

- In running text: **Junkbox**, capital J only. The logo is uppercase; text isn't. Glovo currently says "JunkBox" and Instagram "JunkBoxBulgaria": change both.
- In Bulgarian text: **Джънкбокс**.
- Tagline: **CAFE & FAST FOOD**, always in English and always in caps, as in the logo.
- Handle: **@junkboxbulgaria** everywhere.

## Logo

The Logo component lists every file in `assets/Logos` and where it goes. In short:

- `junkbox-logo-ink.svg` is the primary logo: ink on white or light grounds, with `junkbox-logo-white.svg` for dark grounds.
- `junkbox-tile-amber.svg` is the logo as people know it from the amber file. Use it as the logo on Glovo and Wolt, on post templates and on menu covers.
- `junkbox-avatar.svg` is every profile picture.
- Under 64 px the drawing fills in, so use `junkbox-wordmark-ink.svg` there.
- Only four colourways: ink on white, white on ink, ink on amber, amber on ink.

## Colour

- `amber` (#F7AF0B, from the logo file) is the brand colour. Use it for the logo tile, photo backdrops, posts, the order button and stickers. Text and line art on amber are `on-amber`.
- `ink` (#231F20, the logo's black) is for line art, dark posts and menu boards. Text on ink is `on-ink`; amber can pick out one word.
- Web pages and printed menus are white: `surface`, with cards on `surface-raised` and bands on `surface-sunk`. Text is `text`; ingredients and captions are `text-muted`.
- `hot` is used only for the ЛЮТО tag.
- Never set amber text on white (1.9:1).
- Today there are three ambers in use: the logo file (#F7AF0B), the photo backdrop (#F9B20A) and the Glovo logo tile (#F09C08). Use #F7AF0B for all of them.

## Type

Both faces cover Cyrillic. Write in Bulgarian first and check every layout in Bulgarian.

- **Hand lettering:** item names and headlines in **Neucha**, caps, with the `jb-hand` class. It's the closest Google font to the logo's lettering and a stand-in until the logo's own font is confirmed. Styles: `display-xl`, `display-l`, `display-m`, `title`. One hand-lettered line per post or screen.
- **Montserrat** for everything else:
  - `tagline`: wide-tracked caps for category lines and labels, echoing CAFE & FAST FOOD.
  - `body-l`, `body` and `body-s` for reading.
  - `button` for buttons and tags.
  - `price` for prices.

## Writing

Bulgarian first; item names keep their English names, and the category after them is Bulgarian.

| Today on Glovo | Junkbox 2.0 |
| --- | --- |
| Wild West Бургер + Fries | **Wild West**, телешки бургер + картофки |
| Hot Bandolero Бургер (Нов) + Fries | **Hot Bandolero**, телешки бургер + картофки · НОВО |
| Philly Cheesesteak Tortilla  (NEW) + Fries | **Philly Cheesesteak**, тортила + картофки · НОВО |
| Кесадия Loco + Картофки | **Кесадия Loco** + картофки |

- **Descriptions:** ingredients in one sentence, commas only, no slashes, weight at the end: "Бриош питка, хрупкави пилешки стрипсове, лучени кръгчета, гауда, домашни кисели краставички, домат, айсберг, бургер сос. 380 г".
- **Fix these spellings in every listing:** Ангъс (not Ангьс), чедър (not чедьр), кръгчета (not крьгчета), бриош (not брош), бургер сос (not буого coc), гарнитура (not гарнитира), домашен (not домащен). Coca-Cola is "(500мл)" in the name and "(330мл)" in the description; state the real size once.
- **"New" is НОВО**, as a tag, never in the name.
- **Prices:** "10,99 €".
- **Tone:** short and friendly, with a wink, the way the logo is. Use "ти" on social and "вие" on signs and receipts.

## Photography

Most Glovo photos already put the food on amber. Make it the rule.

- Shoot every item in-house on a seamless backdrop matched to `amber`, one photo per item, the real build that matches the description.
- Use a three-quarter view from about 25° above, a soft shadow straight down, and no props.
- Shoot sides and boxes in their packaging.
- No stock photos, watermarks, or composited flames, smoke or leaves. The current photo for the item called "Junkbox" is a stock image with a Dreamstime watermark: replace it first.
- Until an item has its photo, show the logo illustration on amber (see MenuCard).

## Shape and space

- Square corners: `radius-none` on logo tiles, posts and photos; `radius-sm` on buttons, tags and cards. Round only for stickers and avatar crops.
- Spacing runs on 4px: `space-1` to `space-16`.
- No shadows. Separate things with `line` hairlines or a 2px ink border.
- No icon set; the logo illustration is the only drawing. If a platform needs icons, keep them solid and in ink.

## Packaging

Two inks. Print or stamp the ink illustration (`junkbox-icon-ink.svg`) on kraft bags, boxes and cups, and close each delivery bag with the amber BagSeal sticker.
