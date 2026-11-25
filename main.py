#!/usr/bin/env python3
"""Write the One Line, Big Laugh entry to the output directory.

The entry is a single line, at most 200 characters, with no title,
setup or explanation around it. It is written byte-for-byte to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os

ENTRY = "I asked ChatGPT to roast me, and it just sent back my screen time."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
