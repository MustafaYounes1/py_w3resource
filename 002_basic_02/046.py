"""

Write a Python program that reads a date (from 2016/1/1 to 2016/12/31) and prints the day of the date. Jan. 1, 2016,
is Friday. Note that 2016 is a leap year.

Input:
Two integers m and d separated by a single space in a line, m ,d represent the month and the day.
Input month and date (separated by a single space): 5 15
Name of the date:                                   Sunday

"""

from datetime import date


def main():
    m, d = [int(_) for _ in input("Input month and date (separated by a single space): ").split()]
    day = date(year=2016, month=m, day=d)
    print(f"Name of the date: {day.strftime('%A')}")


if __name__ == "__main__":
    main()
