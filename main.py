#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands - make.fun bounty entry.

Writes one joke about a cat - a setup about what the cat knocks off
the table, with a turn that lands on the punchline - to
/output/entry.txt (the file the make.fun harness grades).
"""

import os

ENTRY = "My cat only knocks off the table the things I love most \u2014 which is how I know she has read my will."

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
