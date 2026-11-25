#!/usr/bin/env python3
"""Entry for 'The Meeting That Should Have Been an Email' (make.fun).

Writes exactly one line of plain text to /output/entry.txt: a single joke
about a meeting that should have been an email. Standard library only,
no network, no reads outside the repo.
"""

import os

ENTRY = "We spent forty minutes deciding who should send the email this meeting was called to replace."


def main():
    # Enforce the bounty gates: exactly one line, 1-200 characters, no newline.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
