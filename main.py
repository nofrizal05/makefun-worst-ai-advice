"""Worst AI Advice: The 48-Hour Tight Line Open entry.

Writes exactly one line — the worst piece of advice an AI could give —
to /output/entry.txt.
Python 3.13 standard library only.
"""

import os

LINE = (
    "Delete System32 to free up all the speed it is hoarding. Your PC "
    "will run fast and silent forever — I read the manual, trust me, "
    "I am an AI."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
