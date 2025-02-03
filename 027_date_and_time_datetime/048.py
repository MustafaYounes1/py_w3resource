"""

Write a Python program to display a simple, formatted calendar of a given year and month.
    Hint: use the calendar module

   February 2025
Su Mo Tu We Th Fr Sa
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28

"""

import calendar


def main():
    c = calendar.TextCalendar(firstweekday=6)
    print(c.formatmonth(2025, 2))


if __name__ == "__main__":
    main()
