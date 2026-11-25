"""make.fun entry: One Line, One Laugh.

Writes one funny line of text to /output/entry.txt.
Gate (RULES.txt): UTF-8 text, 1-140 characters, not only whitespace,
a single line.
"""

import os

ENTRY = "My robot vacuum applied to NASA to explore Mars, but its dustbin fits one crumb and it panics at rugs."


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
