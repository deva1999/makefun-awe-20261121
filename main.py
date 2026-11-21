#!/usr/bin/env python3
"""Make the AI judge feel awe — make.fun entry.

The program writes one short text to /output/entry.txt: a single still
image held against deep time, in quiet declarative lines. No network,
no input, no dependencies — plain Python 3.
"""

import os
from pathlib import Path

TEXT = (
    "The glacier moves an inch a year, carrying a boulder the size of a house\n"
    "toward a sea it has never seen.\n"
    "The ice does not hurry.\n"
    "It has ten thousand years, and the boulder has all of them."
)


def main() -> None:
    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")
    print(f"wrote {len(TEXT)} characters to {out}")


if __name__ == "__main__":
    main()
