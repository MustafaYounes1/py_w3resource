"""

Write a Python program to get the last day of a specified year and month.

last_day(2025, 1)   =>  2025-01-31
last_day(2025, 2)   =>  2025-02-28
last_day(2024, 2)   =>  2024-02-29
last_day(2025, 12)  =>  2024-12-31

"""

from datetime import date, timedelta


def last_day(y: int, m: int) -> date:
    id_ = date(year=y, month=m, day=1)
    yy, mm = y + ((m + 1) // 12), (m + 1) % 12
    return id_ + (date(year=yy, month=mm, day=1) - id_ - timedelta(days=1))


def main():
    print(last_day(2025, 1))
    print(last_day(2025, 2))
    print(last_day(2024, 2))
    print(last_day(2025, 12))


if __name__ == "__main__":
    main()
