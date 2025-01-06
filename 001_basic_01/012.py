"""

Write a Python program that prints the calendar for a given month and year.
Note : Use 'calendar' module.

"""

import calendar


def main():
    my_calendar = calendar.TextCalendar(5)  # 6 is Sunday the last day according to the European Convention
    month, year = input("Input the month and year (separated by a comma): ").split(", ")
    print(my_calendar.formatmonth(int(year.strip()), int(month.strip())))


if __name__ == "__main__":
    main()
