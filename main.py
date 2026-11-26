#!/usr/bin/env python3
"""One Word, One Username, One Reward.

Writes our own make.fun username -- a single word -- to
/output/entry.txt, nothing else. Deterministic: standard library only,
no network, no randomness, so two runs produce identical bytes.
"""

import os

USERNAME = "zesty-condor-95-5960"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(USERNAME) <= 30, "username must be 1-30 characters"
    assert " " not in USERNAME, "username must be a single word"
    assert "\n" not in USERNAME and "\r" not in USERNAME, "username must not contain a newline"
    assert "\t" not in USERNAME, "username must be a single word"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(USERNAME)


if __name__ == "__main__":
    main()
