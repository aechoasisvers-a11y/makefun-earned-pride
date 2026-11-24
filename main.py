"""One Line of Earned Pride — make.fun entry.

Writes a single line of earned pride to /output/entry.txt.
Pure stdlib Python 3.13.
"""

import os

ENTRY = "After eleven failed batches, the night baker pulled the twelfth loaf from the oven, tapped its crust, and heard it sing back."


def main() -> None:
    # Self-check: the brief's gate is 1 to 240 characters, not only
    # whitespace, and the entry must be a single line.
    assert 1 <= len(ENTRY) <= 240, f"entry is {len(ENTRY)} chars, outside 1-240"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

    # Read back and verify the file holds exactly the intended text.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written entry does not match intended text"
    assert 1 <= len(written) <= 240, "written entry outside the char gate"


if __name__ == "__main__":
    main()
