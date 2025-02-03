"""

Write a Python program to count the number of Mondays on the 1st day of the month from 2015 to 2016.

> 3

"""

from datetime import date, timedelta


def month_days(d: date) -> int:
    yy, mm = d.year + d.month // 12, d.month % 12 + 1
    return (date(year=yy, month=mm, day=1) - d.replace(day=1)).days


def add_month(d: date) -> date:
    return d + timedelta(month_days(d))


def n_1st(d: int, y0: int, y1: int) -> int:
    assert d in range(7), "Invalid inputs, day should fall in the range [0 'Mon', 6 'Sun']"
    assert y0 < y1, "Invalid inputs, y0 is expected to be smaller than y1"
    n = 0

    id_ = date(year=y0, month=1, day=1)

    while id_.year <= y1:
        if id_.weekday() == d:
            n += 1
        id_ = add_month(id_)

    return n


def main():
    print(n_1st(0, 2015, 2016))


if __name__ == "__main__":
    main()
