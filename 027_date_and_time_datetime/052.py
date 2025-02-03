"""

Write a Python program to get the first and last time moment.

First second: 00:00:00
Last second:  23:59:59.999999

"""

from datetime import time


def main():
    print(f"First moment: {time.min}")
    print(f"Last moment:  {time.max}")


if __name__ == "__main__":
    main()
