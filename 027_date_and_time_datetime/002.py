"""

Write a Python program to determine whether a given year is a leap year.

1900    =>  False
1992    =>  True
2000    =>  True
2004    =>  True

"""

from datetime import date, timedelta


def is_leap(y: int) -> bool:
    """ A leap year has 366 days (the extra day is the 29th of February), and it comes after every four years.
    A year is a leap year if “any one of” the following conditions are satisfied:
        The year is multiple of 400.
        The year is a multiple of 4 and not a multiple of 100.
    """

    feb_1st = date(year=y, month=2, day=1)
    return (feb_1st + timedelta(days=28)).day == 29

    # Or #

    # if y % 400 == 0:
    #     return True
    #
    # elif y % 100 == 0:
    #     return False
    #
    # elif y % 4 == 0:
    #     return True
    #
    # else:
    #     return False


def main():
    print(is_leap(1900))
    print(is_leap(1992))
    print(is_leap(2000))
    print(is_leap(2004))


if __name__ == "__main__":
    main()
