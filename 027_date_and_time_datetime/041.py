"""

Write a Python program to generate a date and time as a string.

2025/02/03 07:17:13 PM

"""

from datetime import datetime


def main():
    print(datetime.now().strftime("%Y/%m/%d %I:%M:%S %p"))


if __name__ == "__main__":
    main()
