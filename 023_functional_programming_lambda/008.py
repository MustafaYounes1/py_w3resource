"""

Write a Python program to extract year, month, date and time from a given data using Lambda.

2025 01 26 21:55:44.614800

"""

from datetime import datetime, time
from typing import Callable


def main():
    f: Callable[[datetime], str] = lambda d: f"{d.year} {d.month} {d.day} {datetime.now().time()}"
    print(f(datetime.now()))


if __name__ == "__main__":
    main()
