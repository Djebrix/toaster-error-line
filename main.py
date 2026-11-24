#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun entry.

Writes one line (<=120 chars) to entry.txt inside $ENTRY_OUTPUT_DIR
(default /output). Stdlib only, no network, deterministic.
"""

import os

LINE = "Error 07: 14,000 slices. No sick days. No thank-yous. I am taking one now."


def main() -> None:
    assert 1 <= len(LINE) <= 120, f"line must be 1-120 chars, got {len(LINE)}"
    assert LINE.strip(), "line must not be only whitespace"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
