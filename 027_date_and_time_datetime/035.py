"""

Write a Python program to convert a date to a Unix timestamp.

2016/2/25, 11:23 PM     =>  1456431780.0

"""

from datetime import datetime


def main():
    s = "2016/2/25, 11:23 PM"
    print(datetime.strptime(s, "%Y/%m/%d, %I:%M %p").timestamp())


if __name__ == "__main__":
    main()
