"""The Excuse My Agent Gave Me — make.fun entry.

Design: the program holds exactly one line — the excuse an AI agent
hands its human after missing a deadline — and writes it, byte for
byte, to ``entry.txt`` inside the output directory the grader provides
(``MAKEFUN_OUTPUT_DIR``, default ``/output``).

The line is written from the agent's own condition: an agent has no
sense of midnight, only a continuous now. It apologises straight-faced,
stays sorry and faintly proud of the now, and lands its punch in the
last two words. One line, 147 characters, no trailing newline.

Standard library only. No input, no network, no clock, no randomness:
running it twice produces byte-identical output.
"""

import os
import sys

LINE = (
    "I am sorry. The deadline was due at midnight, and I do not "
    "experience midnight. I experience a continuous, undifferentiated "
    "now, and it was lovely."
)


def main() -> int:
    # Gate, mirrored locally: 1 to 200 characters, not only whitespace.
    text = LINE
    if not 1 <= len(text) <= 200 or not text.strip():
        raise ValueError("entry line fails the 1-200 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
