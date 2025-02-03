"""

Write a Python program to get the current time in milliseconds in Python.

2025-02-02 19:14:42.272580 -> 1738512882272.5806

"""

from datetime import datetime
import time


def main():
    print(f"{datetime.now()} -> {time.time() * 1e3}")


if __name__ == "__main__":
    main()
