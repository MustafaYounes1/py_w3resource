"""

Write a Python program to add a month to a specified date.
    Note: the amount of days to be added should be inferred from how many days the current month has (28, 29, 30, or 31)

2014, 12, 25    =>  2015-01-25

"""

from datetime import date, datetime, timedelta


def month_days(d: date) -> int:
    yy, mm = d.year + d.month // 12, d.month % 12 + 1
    return (date(year=yy, month=mm, day=1) - d.replace(day=1)).days


def add_month(d: date) -> date:
    return d + timedelta(month_days(d))


def main():
    s = "2014, 12, 25"
    print(add_month(datetime.strptime(s, "%Y, %m, %d").date()))


if __name__ == "__main__":
    main()
