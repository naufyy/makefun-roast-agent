"""Entry for make.fun 'Roast Your Own Agent' (u-nayyy-roast-your-own-agent-4c3d413c).

Writes the winning one-line roast to /output/entry.txt (UTF-8, no trailing
newline added by this program beyond the string itself).
The line roasts the maker's own agent: asked for one line, it produced six
candidates, ran a selection tournament, and picked the entry about itself.
Deterministic: same bytes on every run.
"""

from pathlib import Path

ENTRY = "I asked my agent for one line; it wrote six candidates, held a tournament, and submitted the one about itself asking for approval."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
