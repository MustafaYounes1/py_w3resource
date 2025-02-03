"""

Write a Python program to get the third Tuesday of a month.

2025-02  =>  2025-02-18, Tue

"""

from datetime import date, timedelta


def get_nth_day(year: int, month: int, day: int, n: int) -> date:
    assert day in range(7), "weekday should fall in the range [0, 6]"

    id_ = date(year=year, month=month, day=1)
    d_off = (day - id_.weekday()) % 7
    id_ += timedelta(days=d_off)

    id_ += timedelta(days=7 * (n - 1))
    assert id_.month == month, f"invalid n: {n}"

    return id_


def main():
    d = get_nth_day(2025, 2, 1, 3)
    print(f"{d}, {d.strftime('%a')}")


if __name__ == "__main__":
    main()
