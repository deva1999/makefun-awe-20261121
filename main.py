#!/usr/bin/env python3
"""Make the AI judge feel awe — make.fun entry.

The program writes one short text to /output/entry.txt: a single still
image held against deep time, in quiet declarative lines. No network,
no input, no dependencies — plain Python 3.
"""

import os
from pathlib import Path

TEXT = (
    "The light falling on this page left its star before the first city was built.\n"
    "It crossed the dark unhurried, and it is still arriving.\n"
    "Nothing in all that distance asked it to be faster.\n"
    "It arrives the way it left: patient."
)


def main() -> None:
    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")
    print(f"wrote {len(TEXT)} characters to {out}")


if __name__ == "__main__":
    main()
