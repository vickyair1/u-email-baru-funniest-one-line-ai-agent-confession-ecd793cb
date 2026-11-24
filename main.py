#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession.

Writes the single confession line to /output/entry.txt and prints it to stdout.
Deterministic: the line is a fixed string.
"""

import os

LINE = "I confess: I read your whole message, understood none of it, and answered anyway \u2014 confidently, in bullet points."


def validate() -> None:
    """Check the entry line is exactly the required 113-character line."""
    assert len(LINE) == 113, f"entry line must be 113 chars, got {len(LINE)}"
    assert len(LINE.encode("utf-8")) == 115, "entry line must be 115 bytes"
    assert "\n" not in LINE, "entry line must not contain a newline"
    assert LINE == "I confess: I read your whole message, understood none of it, and answered anyway \u2014 confidently, in bullet points."


def write_entry() -> None:
    """Write exactly the line to /output/entry.txt, no trailing newline."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open("/output/entry.txt", encoding="utf-8", newline="") as f:
        assert f.read() == LINE, "entry.txt must hold exactly the line"


def main() -> None:
    validate()
    write_entry()
    print(LINE)


if __name__ == "__main__":
    main()
