# Button

The order button: amber, ink border, the sticker shadow, and it "presses" into the page when tapped.

- **Provide:** a `<button class="jb-btn">` with a verb in Bulgarian, uppercase via CSS. Add `<span class="jb-btn-price">` for a price on the button.
- **Variants:** default amber for the one main action per screen (Поръчай, Добави). `jb-btn--ink` for secondary navigation (Виж менюто). `jb-btn--ghost` for low-stakes extras (Добави сос). `disabled` when the kitchen is closed.
- **Do:** one amber button per view. Keep labels to one or two words.
- **Don't:** put an amber button on an amber ground; use `jb-btn--ink` there. Don't remove the focus ring (3px `focus`, 2px offset).
