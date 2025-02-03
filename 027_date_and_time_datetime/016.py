"""

Write a Python program to add year(s) to a given date and display the updated date.

Date:   2015,1,1

-1  =>  2014-01-01
0   =>  2015-01-01
2   =>  2017-01-01
1   =>  2016-01-01

"""

from datetime import date, datetime


def add_years(d: date, y: int) -> date:
    try:
        return d.replace(year=d.year + y)

    except ValueError:
        # Adjust for leap year when moving to non-leap year (e.g. Feb 29)
        return d.replace(year=d.year + y, day=28)


def main():
    d = datetime.strptime("2015,1,1", "%Y,%m,%d").date()
    print(add_years(d, -1))
    print(add_years(d, 0))
    print(add_years(d, 2))
    print(add_years(d, 1))


if __name__ == "__main__":
    main()
