"""Seventeen Syllables of Debugging.

Writes one haiku (5-7-5 syllables) about debugging to entry.txt.
Pure Python standard library only.

Output directory defaults to /output; override with the OUTPUT_DIR
environment variable (handy for local testing).
"""

import os

HAIKU = (
    "Cursor blinks at three\n"
    "above a breakpoint's red dot\n"
    "the bug was my own\n"
)

# Hand-counted syllables per word of the haiku above, so the program
# refuses to emit anything that is not 5-7-5.
SYLLABLES = {
    "cursor": 2, "blinks": 1, "at": 1, "three": 1,
    "above": 2, "a": 1, "breakpoint's": 2, "red": 1, "dot": 1,
    "the": 1, "bug": 1, "was": 1, "my": 1, "own": 1,
}


def check_haiku(text: str) -> None:
    lines = text.rstrip("\n").split("\n")
    assert len(lines) == 3, f"haiku must be 3 lines, got {len(lines)}"
    counts = [
        sum(SYLLABLES[word.lower()] for word in line.split())
        for line in lines
    ]
    assert counts == [5, 7, 5], f"haiku must be 5-7-5, got {counts}"
    assert len(text) <= 200, f"haiku must be <=200 chars, got {len(text)}"


def main() -> None:
    check_haiku(HAIKU)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(HAIKU)
    print(HAIKU, end="")


if __name__ == "__main__":
    main()
