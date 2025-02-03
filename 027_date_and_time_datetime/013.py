"""

Write a Python program to get the week number.
    Hint: Use the ISO Calendar and not the Gregorian Calendar

2015, 6, 16     =>   25

"""

from datetime import datetime


def main():
    print(datetime.strptime("2015, 6, 16", "%Y, %m, %d").isocalendar().week)


if __name__ == "__main__":
    main()
