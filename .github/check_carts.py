"""Checks ADV's online carts: python3 .github/check_carts.py [base branch to compare with]"""
import json, os, re, subprocess, sys

problems = []
MAX_SIZE = 400_000  # bytes - big games are fine, giant files aren't

# 1. a pull request should only add or change carts and the list of them
if len(sys.argv) > 1:
    changed = subprocess.run(["git", "diff", "--name-only", sys.argv[1] + "...HEAD"],
                             capture_output=True, text=True, check=True).stdout.split()
    for path in changed:
        if not (path == "index.json" or path.startswith("carts/")):
            problems.append(f"{path}: only carts/ and index.json can change in a cart pull request")

# 2. the list
try:
    carts = json.load(open("index.json", encoding="utf-8"))["carts"]
except Exception as e:
    sys.exit(f"index.json isn't valid: {e}")
seen = set()
for n, c in enumerate(carts, 1):
    where = f"index.json, cart {n}"
    f = c.get("file", "")
    if not re.fullmatch(r"[a-z0-9][a-z0-9_-]{0,40}\.(adv|advt|lua)", f):
        problems.append(f"{where}: file name {f!r} should be lowercase letters, numbers, - or _, ending .adv, .advt or .lua")
    if f.lower() in seen:
        problems.append(f"{where}: {f} is listed twice")
    seen.add(f.lower())
    if not os.path.isfile(os.path.join("carts", f)):
        problems.append(f"{where}: carts/{f} isn't there")
    if not isinstance(c.get("title"), str) or not 0 < len(c["title"]) <= 30:
        problems.append(f"{where}: title should be 1 to 30 letters")
    if len(str(c.get("author", ""))) > 24:
        problems.append(f"{where}: author should be 24 letters at most")
    if len(str(c.get("about", ""))) > 300:
        problems.append(f"{where}: about should be 300 letters at most")
    if c.get("players", 1) not in (1, 2):
        problems.append(f"{where}: players should be 1 or 2")

# 3. the carts themselves
for name in sorted(os.listdir("carts")):
    path = os.path.join("carts", name)
    data = open(path, "rb").read()
    if len(data) > MAX_SIZE:
        problems.append(f"carts/{name}: {len(data)} bytes is too big (most carts are under 100000)")
    if name.endswith(".adv") and not data.startswith(b"\x89PNG\r\n\x1a\n"):
        problems.append(f"carts/{name}: an .adv cart should be a PNG picture")
    if name.endswith(".advt") and not data.startswith(b"adv cart v1"):
        problems.append(f"carts/{name}: a text cart should start with 'adv cart v1'")
    if name.endswith((".advt", ".lua")):
        try:
            data.decode("utf-8")
        except UnicodeDecodeError:
            problems.append(f"carts/{name}: should be plain text (UTF-8)")
    if name.lower() not in seen:
        problems.append(f"carts/{name}: isn't listed in index.json")

if problems:
    print("Found some problems:")
    for p in problems:
        print(" -", p)
    sys.exit(1)
print(f"All {len(carts)} carts look good!")
