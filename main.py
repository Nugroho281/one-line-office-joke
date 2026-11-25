"""One-Line Office Joke: 24-Hour Sprint.

Writes the winning one-line office joke to /output/entry.txt.
Pure standard library only.
"""

import os

JOKE = (
    "I told HR my spirit animal is the office printer: "
    "I only work when someone stands over me and threatens to replace me."
)


def main():
    # Gate self-check: 1-200 chars, single line, not only whitespace.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert "\n" not in JOKE and JOKE.strip(), "joke must be one non-blank line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
