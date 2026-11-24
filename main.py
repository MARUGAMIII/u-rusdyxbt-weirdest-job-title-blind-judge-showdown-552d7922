"""Weirdest Job Title: Blind Judge Showdown — make.fun entry.

Writes a single weird job title (60 characters max, plain ASCII) to
/output/entry.txt. Deterministic: the same title on every run.
"""

import os

# Final title: same real-sounding job frame, but the client is narrowed
# from "Billionaires" to "Billionaires' Exes" — a second, more specific
# twist that is funnier on first read and easier to picture: someone hired
# to apologize to a billionaire's ex-partners.
TITLE = "Professional Apologizer for Billionaires' Exes"


def main() -> None:
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(TITLE)


if __name__ == "__main__":
    main()
