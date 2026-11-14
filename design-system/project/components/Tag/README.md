# Tag

Short uppercase labels on menu cards, posts and listings. There are exactly five; don't invent more.

| Class | Text | Meaning |
| --- | --- | --- |
| `jb-tag` | НОВО | Added in the last 30 days. Replaces "(Нов)", "(Ново)" and "(NEW)", which are all in use on Glovo today. |
| `jb-tag--combo` | КОМБО | A menu with two or more mains and drinks (Double Trouble, Samurai Jack, Quadra Kill). |
| `jb-tag--veg` | ВЕДЖИ | No meat. Uses `pickle`. |
| `jb-tag--hot` | ЛЮТО | Heat 2 or 3 on the heat meter. Uses `chili`. |
| `jb-tag--weight` | 380 г | Portion weight, mono. Every main carries one. |

- **Provide:** a `<span>` with the word; CSS sets the case.
- **Don't:** use more than three tags on one item, or put tags in the item name. On delivery apps, where you can't style tags, write them at the start of the description: "НОВО · 380 г ·".
