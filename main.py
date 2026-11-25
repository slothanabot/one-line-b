"""make.fun entry: One Line, One Laugh.

Writes one funny line of text to /output/entry.txt.
Gate (RULES.txt): UTF-8 text, 1-140 characters, not only whitespace,
a single line.

How the line meets the judge brief (laugh first, then turn, tightness,
freshness, clarity):
- Laugh / turn: a robot vacuum applies to NASA to explore Mars, then
  the line collapses its ambition in two descending beats -- it panics
  at ordinary rugs, and its dustbin fits a single crumb.
- Tightness: every clause earns its place; the punchline (the tiny
  dustbin, the entry's angle) lands last, so the joke ends on its
  smallest, funniest image.
- Freshness: the joke is not a stock vacuum pun; the absurd job
  application (NASA) against a household appliance is the surprise.
- Clarity: plain words, one breath, no explanation needed.
"""

import os

ENTRY = "My robot vacuum applied to NASA to explore Mars, but it panics at rugs and its dustbin fits one crumb."


def verify(text):
    """Enforce the gate: 1-140 chars, non-blank, single line."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not (1 <= len(text) <= 140):
        raise ValueError("entry must be 1-140 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return True


def write_entry(path="/output/entry.txt"):
    """Write ENTRY plus a trailing newline to path."""
    verify(ENTRY)
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    return path


def main():
    verify(ENTRY)
    print("chars: %d" % len(ENTRY))
    print(ENTRY)
    write_entry()


if __name__ == "__main__":
    main()
