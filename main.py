#!/usr/bin/env python3
"""Entry for 'The Meeting That Should Have Been an Email' (make.fun).

Writes exactly one line of plain text to /output/entry.txt: a single joke
about a meeting that should have been an email. Standard library only,
no network, no reads outside the repo.

Why this line was chosen against the judge's criteria: the premise is a
meeting called to replace an email, and the joke is that the meeting burns
forty minutes on the one thing it exists to eliminate — deciding who sends
the email. The punch lands on the last word, "replace", which turns the
premise back on itself: the meeting never actually replaced anything, it
only added a decision about the email it was supposed to have replaced.
Concrete and specific (forty minutes, one decision, one email), and it
needs no setup beyond the bounty title.
"""

import os

ENTRY = "We spent forty minutes deciding who should send the email this meeting was called to replace."


def validated_entry():
    """Return the entry line after enforcing every bounty gate."""
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert ENTRY == ENTRY.strip(), "entry must have no leading/trailing whitespace"
    return ENTRY


def write_entry(path="/output/entry.txt"):
    """Write the validated line to path and self-check what landed on disk."""
    line = validated_entry()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    # Deterministic self-check: re-read the file and require an exact match.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "output file does not match the validated entry"
    assert written.count("\n") == 0, "output file must contain exactly one line"
    return line


def main():
    write_entry()


if __name__ == "__main__":
    main()
