"""

Write a Python program that checks whether a given year is a leap year or not using boolean logic.

2000    ->  True
2021    ->  False

"""

from datetime import date, timedelta


def is_leap(y: int) -> bool:
    feb_1st = date(year=y, month=2, day=1)
    return (feb_1st + timedelta(days=28)).day == 29


def main():
    data = [2000, 2021]

    for _ in data:
        print(is_leap(_))


if __name__ == "__main__":
    main()
