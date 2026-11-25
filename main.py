#!/usr/bin/env python3
"""One-Line Office Jokes — entry program.

Writes a single original one-line office joke to
$MAKEFUN_OUTPUT_DIR/entry.txt (UTF-8, one line, 1-199 chars).
Stdlib only; no network, no external assets.
"""

import os
import sys

JOKE = (
    "Our printer jammed on my resignation letter, so HR thinks "
    "I changed my mind and the printer thinks it saved me."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = JOKE.strip()
    if not 1 <= len(text) <= 199:
        print(f"joke length {len(text)} out of range 1-199", file=sys.stderr)
        return 1
    if "\n" in text:
        print("joke must be a single line", file=sys.stderr)
        return 1
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")
    os.chmod(path, 0o644)
    # Read back and confirm exactly what the judge will see.
    with open(path, "r", encoding="utf-8") as fh:
        saved = fh.read()
    if saved.strip() != text or len(saved.strip()) > 199:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
