"""

Write a Python program to validate a Gregorian date. The month is between 1 and 12 inclusive, the day is within the
allowed number of days for the given month. Leap year's are taken into consideration. The year is between MINYEAR and
MAXYEAR inclusive.

m,  d,  y
11, 11, 2002        =>  True
13, 11, 2002        =>  False

"""

from datetime import date


def validate_date(m: int, d: int, y: int) -> bool:
    try:
        _ = date(y, m, d)
        return True

    except ValueError:
        return False


def main():
    print(validate_date(11, 11, 2002))
    print(validate_date(13, 11, 2002))


if __name__ == "__main__":
    main()
