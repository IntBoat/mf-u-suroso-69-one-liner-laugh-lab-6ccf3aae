"""Write the one-liner entry to /output/entry.txt.

The entry is a single funny line of at most 200 characters, written
exactly as-is with no trailing newline.
"""

import os

ENTRY = "It wasn't a snack, it was a hostage negotiation — the sock started it by lying on the floor looking delicious."


def main():
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
