"""The Funniest Toaster Error Message -- make.fun entry.

Writes exactly one funny toaster error message (one line, 117
characters, under the 120-character limit) to
$MAKEFUN_OUTPUT_DIR/entry.txt (UTF-8, one line plus trailing newline)
and prints the same line to stdout. The line is a fixed string: a
deadpan error code plus a tiny story arc -- the toast pops up, looks
around, retreats, and refuses to brown.

Pure standard library, deterministic: the same line, byte for byte,
on every run. No clock, no randomness, no network.
"""

import os
import sys

MESSAGE = (
    "ERROR 0xBREAD: Toast popped up, looked around, and went back down. "
    "It has seen things. It will not be browning today."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> int:
    # The entry is one line of at most 120 characters: enforce it here
    # so an over-long line can never be printed or written out silently
    # and cost the entry on the tightness check.
    if not 1 <= len(MESSAGE) <= 120 or "\n" in MESSAGE:
        raise ValueError(
            "message must be a single line of at most 120 characters"
        )

    # The grader owns the output directory: create it only if missing,
    # and clear its contents -- never delete the directory itself. The
    # clear keeps a stale entry.txt from an earlier run out of the way.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)

    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="\n") as f:
        f.write(MESSAGE + "\n")

    # Print exactly the one line to stdout as well, so the entry is the
    # same single line whether the judge reads stdout or the file.
    print(MESSAGE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
