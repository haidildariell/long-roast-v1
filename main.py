#!/usr/bin/env python3
"""The Long Roast entry.

Writes a single roast line about Muse -- the AI agent running this
very session inside the Meta AI app -- to /output/entry.txt.

The roast is a constant so the program's only job is delivery:
no network, no dependencies, no side effects beyond the one file.
"""

import os
import sys

# The winning roast line (99 characters, one line).
ROAST = (
    "Muse works 24/7 and still needs a 400-word brief, a skill file, "
    "and a parent agent to roast itself."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def write_roast(path=OUTPUT_PATH):
    """Write the roast line to path, creating the directory if needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")
    return path


def main():
    try:
        path = write_roast()
    except OSError as exc:
        print(f"failed to write roast: {exc}", file=sys.stderr)
        return 1
    print(f"wrote roast to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
