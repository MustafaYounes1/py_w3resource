"""

Write a Python program that calculates the date six months from the current date using the datetime module.
    Note:   the amount of days to be deleted should be inferred from how many days the current month has
            (28, 29, 30, or 31)

Current Date:               2025-02-03
After subtracting 6 months: 2024-08-06

"""

from datetime import date, timedelta


def month_days(d: date) -> int:
    y, m = d.year + d.month // 12, d.month % 12 + 1
    return (date(year=y, month=m, day=1) - d.replace(day=1)).days


def subtract_month(d: date) -> date:
    return d - timedelta(month_days(d))


def main():
    d = date.today()
    print(f"Current Date:               {d}")

    for _ in range(6):
        d = subtract_month(d)

    print(f"After subtracting 6 months: {d}")


if __name__ == "__main__":
    main()
