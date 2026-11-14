Junkbox is a street-food counter at Пиротска 61, Sofia. It sells brioche burgers, tortillas, quesadillas and fried boxes, mostly through Glovo, under menu names borrowed from action films and video games: Samurai Jack, Wild West, Hot Bandolero, Double Cheese-murder, Quadra Kill. This system keeps the two things the brand already owns, the amber backdrop and that naming voice, and replaces everything else: the trash-can logo, the stock photos and the mixed-up copy.

## The brand in one line

**Street food with a fighter's name.** Every item is a character, every combo is a move, and everything comes in a box with a bite already taken out of it.

## Name

- In running text: **Junkbox**, one word, capital J only. Not JunkBox, Junk Box or JUNKBOX. Glovo, Instagram and the logo use all three today.
- In Bulgarian running text: **Джънкбокс**.
- Handle: **@junkboxbulgaria** on every platform.
- The logo is always uppercase; that is the logo, not the spelling.

## Logo

Use the files in `assets/Logos`; the Logo component lists which one goes where. The primary mark is `junkbox-boxmark.svg`: an `amber` box with a bite out of its top-right corner, JUNK over BOX in `on-amber`. Round profile pictures use `junkbox-avatar.svg`. Kraft packaging uses the one-ink `junkbox-stamp.svg`. Never redraw the mark; the letters are outlined from Dela Gothic One.

Retire the old logo everywhere: the hand-lettered JUNKBOX on an orange rounded tile with an engraved trash can overflowing with food (see `assets/Audit/current-logo.jpg`).

## Colour

- `amber` is the brand. Use it big: photo backdrops, the logo box, posts, stickers, the order button. Text on amber is always `on-amber`.
- `ink` is the second brand colour: story backgrounds, price tags, the stamp, dark menu boards. Text on ink is `on-ink`, with one word in `amber` at most.
- Web and print pages sit on `surface`, with cards on `surface-raised` and bands on `surface-sunk`. Text is `text`, secondary text `text-muted`.
- `kraft` is the packaging colour. It is never a screen background.
- `pickle` means veggie or fresh, nothing else. `chili` means heat, nothing else. Neither is ever used for prices, sales or errors.
- Never set `amber` as text on a light ground (1.8:1). Never put white on amber.
- Focus is a 3px solid `focus` ring with a 2px offset.

## Type

All three faces cover Cyrillic. Bulgarian comes first, so test every layout in Bulgarian before English.

- **Dela Gothic One** (`display`) is for item names and headlines only, in caps. One display line per post, poster or screen. Styles: `display-xl`, `display-l`, `display-m`, `title`.
- **Onest** (`sans`) is for everything people read: descriptions, captions, buttons. Styles: `body-l`, `body`, `body-s`, `label`.
- **Martian Mono** (`mono`) is the kitchen ticket. Use it for prices, grams, order numbers and times. Styles: `price`, `ticket`.

## Writing

**Bulgarian first, English names.** Item names stay in their English hero form; the category that follows is Bulgarian.

| Today on Glovo | Junkbox 2.0 |
| --- | --- |
| Wild West Бургер + Fries | **Wild West**, телешки бургер + картофки |
| Hot Bandolero Бургер (Нов) + Fries | **Hot Bandolero**, телешки бургер + картофки · НОВО |
| Philly Cheesesteak Tortilla  (NEW) + Fries | **Philly Cheesesteak**, тортила + картофки · НОВО |
| Самурай Бургер / Samurai Jack Меню | **Samurai**, пилешки бургер / **Samurai Jack**, комбо за двама |

**Description format.** Ingredients as one sentence in serving order, commas only, no slashes, then the weight: "Бриош питка, хрупкави пилешки стрипсове, лучени кръгчета, гауда, домашни кисели краставички, домат, айсберг, бургер сос. 380 г". Name the side separately, never inside the slashes.

**Spelling to fix in every listing:** Ангъс (not Ангьс), чедър (not чедьр), кръгчета (not крьгчета), бриош (not брош), бургер сос (not буого coc), гарнитура (not гарнитира), домашен (not домащен). Coca-Cola is listed as "(500мл)" with the description "(330мл)": state the real size once.

**Names are the voice.** Keep naming new items and combos as characters and moves: films, westerns, fighting games, MOBA kill streaks. One name per item; no puns in descriptions. Descriptions stay plain and appetising.

**Tone.** Short, confident, a bit of swagger. Speak to the eater with "ти" on social and "вие" on official signs and receipts. No emoji in names or on packaging. On social, use one at most and never as a bullet.

**Prices:** "10,99 €". Comma decimal, a space, then the € sign.

## Photography

The amber sweep is the house style; 14 of the 20 Glovo photos already use it. Make it a rule.

- Every menu item is photographed in-house, on a seamless backdrop matched to `amber`. One photo per item; two items never share a photo.
- Camera at about 25° above the plate, three-quarter view, the cut side facing camera for tortillas and quesadillas. Soft shadow straight down. No props on the main shot.
- Shoot the real build that matches the description. Stay Strong shows slaw today, but the recipe lists айсберг and домат.
- Sides and boxes are shot in their kraft packaging.
- No stock photography, no watermarks, no composited flames, smoke or flying leaves. The current photo for the item named "Junkbox" is a stock image with a Dreamstime watermark showing wings and coleslaw that aren't on the menu. Replace it first.
- Crop photos square for menus and listings; add the bite to the corner with the `jb-bite` class.

## The bite

The bite is the brand's graphic device: three overlapping circles cut from a top-right corner. It goes on the logo, photo crops, price tags, the bag seal and stickers. Always top-right, and only one per object. In CSS, add `jb-bite` and set `--bite` to the tooth radius (about 7% of the shorter side).

## Shape, space and depth

- Corners are square-shouldered: `radius-md` on cards, photos and buttons, `radius-sm` on tags and price tags, `radius-pill` only for heat segments and round stickers.
- Spacing runs on 4px: `space-1` to `space-16`.
- There is one shadow, `shadow-sticker`: hard, offset, no blur. Use it on stickers, price tags and the order button. Cards get `line` hairlines instead.
- Motion: buttons press down (shadow collapses) on tap; nothing else animates. Respect reduced motion.

## Iconography

The source has no icon set, and this system doesn't add one. Heat is the HeatMeter, labels are Tags, and the bite is the only ornament. If a platform demands icons, use simple solid shapes in `ink` or `on-amber`; no outline icon sets and no emoji.

## Packaging

Two inks: the `junkbox-stamp.svg` stamp on kraft boxes, bags and fry cups, plus the amber BagSeal sticker closing each delivery bag. Napkins and tape use the ink wordmark.
