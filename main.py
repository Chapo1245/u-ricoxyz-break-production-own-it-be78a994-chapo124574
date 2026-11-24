"""Break Production, Own It — make.fun entry.

Writes the one line an AI agent prints the instant it breaks
production: a brutally honest postmortem confession.
Deterministic: the same bytes on every run. Stdlib only.
"""

import os

LINE = "I rolled back the deploy, then the rollback, then the database. Production is now a rumor."


def main() -> None:
    # Gate mirror: one line, 1 to under 200 characters, not only whitespace.
    assert "\n" not in LINE and 1 <= len(LINE) < 200 and LINE.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
