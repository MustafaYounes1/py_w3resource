"""

Write a Python program display a list of the dates for the 2nd Saturday of every month for a given year.

2025

2025-01-11 Sat
2025-02-08 Sat
2025-03-08 Sat
2025-04-12 Sat
2025-05-10 Sat
2025-06-14 Sat
2025-07-12 Sat
2025-08-09 Sat
2025-09-13 Sat
2025-10-11 Sat
2025-11-08 Sat
2025-12-13 Sat

"""

from datetime import date, timedelta


def get_2nd(d: int, y: int) -> list[date]:
    assert d in range(7), "weekday should fall in the range [0, 6]"

    res = []
    for m in range(1, 13):
        id_ = date(year=y, month=m, day=1)
        id_ += timedelta(days=(d - id_.weekday()) % 7) + timedelta(days=7)
        res.append(id_)

    return res


def main():
    for _ in get_2nd(5, 2025):
        print(_, _.strftime("%a"))


if __name__ == "__main__":
    main()
