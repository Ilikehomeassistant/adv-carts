# ADV carts

Online cartridges for **ADV**, a little fantasy console.

ADV's cart library reads `index.json` and downloads carts from `carts/`.
Every `.adv` file is a real PNG picture - rename it to `.png` to see the game hidden inside.

## Adding a cart
1. Put the `.adv` file in `carts/`.
2. Add an entry to `index.json`:
   ```json
   {"file": "mygame.adv", "title": "my game", "author": "me", "players": 1, "about": "what it is"}
   ```
