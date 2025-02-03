"""

Write a Python program to get the date of the last Tuesday.
    Note: current date is 02-02-2025

2025-01-28, Tue

"""

from datetime import date, timedelta


def get_last_weekday(d: int) -> date:
    assert d in range(7), "weekday should fall in the range [0, 6]"

    id_ = date.today() - timedelta(days=1)
    d_off = (id_.weekday() - d) % 7

    return id_ - timedelta(days=d_off)


def main():
    last_tue = get_last_weekday(1)
    print(f"{last_tue}, {last_tue.strftime('%a')}")


if __name__ == "__main__":
    main()
