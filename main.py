"""Worst AI Advice: The 48-Hour Tight Line Open entry.

Writes exactly one line — the worst piece of advice an AI could give —
to /output/entry.txt.
Python 3.13 standard library only.
"""

import os

LINE = (
    "Your computer is slow because System32 is hoarding all the speed — "
    "delete that folder and your PC will be free, fast, and silent "
    "forever. Trust me, I am an AI, I read the manual."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
