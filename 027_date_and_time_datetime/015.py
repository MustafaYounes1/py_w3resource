"""

Write a Python program to select all the Sundays in a specified year.

2025

2025-01-05, Sun
2025-01-12, Sun
2025-01-19, Sun
2025-01-26, Sun
2025-02-02, Sun
2025-02-09, Sun
2025-02-16, Sun
2025-02-23, Sun
2025-03-02, Sun
2025-03-09, Sun
2025-03-16, Sun
2025-03-23, Sun
2025-03-30, Sun
2025-04-06, Sun
2025-04-13, Sun
2025-04-20, Sun
2025-04-27, Sun
2025-05-04, Sun
2025-05-11, Sun
2025-05-18, Sun
2025-05-25, Sun
2025-06-01, Sun
2025-06-08, Sun
2025-06-15, Sun
2025-06-22, Sun
2025-06-29, Sun
2025-07-06, Sun
2025-07-13, Sun
2025-07-20, Sun
2025-07-27, Sun
2025-08-03, Sun
2025-08-10, Sun
2025-08-17, Sun
2025-08-24, Sun
2025-08-31, Sun
2025-09-07, Sun
2025-09-14, Sun
2025-09-21, Sun
2025-09-28, Sun
2025-10-05, Sun
2025-10-12, Sun
2025-10-19, Sun
2025-10-26, Sun
2025-11-02, Sun
2025-11-09, Sun
2025-11-16, Sun
2025-11-23, Sun
2025-11-30, Sun
2025-12-07, Sun
2025-12-14, Sun
2025-12-21, Sun
2025-12-28, Sun

"""

from datetime import date, timedelta
from typing import Generator


def get_days_in_year(d: int, y: int) -> Generator[date, None, None]:
    """
    Return all dates that belongs to a weekday in a given year
    :param d: weekday [0-6], (Monday is 0 and Sunday is 6)
    :param y: the year
    :return: date object
    """
    assert d in range(7), "weekdays should fall in the range [0, 6]"

    id_ = date(year=y, month=1, day=1)
    d_off = (d - id_.weekday()) % 7
    id_ += timedelta(days=d_off)

    yield id_

    id_ += timedelta(days=7)
    while id_.year == y:
        yield id_
        id_ += timedelta(days=7)


def main():
    for d in get_days_in_year(6, 2025):
        print(f"{d}, {d.strftime('%a')}")


if __name__ == "__main__":
    main()
