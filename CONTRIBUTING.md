# Making a game for ADV

Anyone can make a game for ADV and send it here. Once it's accepted, it shows up on
everyone's online screen: on the website, in the Windows app and on the phone.

## 1. Make it
- **In your browser:** open the [Developer Kit](https://ilikehomeassistant.github.io/adv-web/devkit.html) on a PC.
  - *The easy way:* in the sprite editor, click **IT IS...** to say what a sprite is
    (player, enemy, flyer, collect, solid, hurts, goal, bouncy, heart, save or climb), paint them on the map, and press CTRL+R.
  - *The advanced way:* write Lua in the code editor, and make sounds and music. You can mix in Scratch-style blocks too.
- **On Windows:** [download the Developer Kit](https://github.com/Ilikehomeassistant/adv-web/releases/latest/download/ADV-DevKit-Windows.zip), with the same editors.

## 2. Send it
- **From the Developer Kit:** type **UPLOAD** with your cart in the slot (or click **UPLOAD TO ADV ONLINE**). It uses your own GitHub account
  to make a copy of this repo, adds your cart, and opens a pull request. Commits use
  GitHub's private "noreply" email, so your email isn't shown.
- **By hand:** fork this repo, put your cart in `carts/`, add a line to `index.json`, and open a pull request:
  ```json
  {"file": "mygame.advt", "title": "my game", "author": "me", "players": 1, "about": "what it is"}
  ```

## What gets checked
A robot checks every pull request:
- only `carts/` and `index.json` change;
- carts are real carts, under 400 KB;
- every line in the list is filled in.

Then the owner of ADV plays it. Keep it friendly for everyone, and only send games you made (or are allowed to share).

The name you give as **author** is shown to everyone, so a nickname is a good idea.
