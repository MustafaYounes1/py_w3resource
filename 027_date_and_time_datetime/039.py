"""

Write a Python program to calculate an age in (years, week, and days).
    Current date:   2025-02-03

2006-10-12      =>  18 year, 16 weeks, 2 days
1996-11-01      =>  28 year, 13 weeks, 3 days

"""

from datetime import date, datetime


def get_age(d: date) -> tuple[int, int, int]:
    s = (date.today() - d).total_seconds()
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    y, d = divmod(d, 365.25)
    w, d = divmod(d, 7)
    return int(y), int(w), int(d)


def main():
    data = ["2006-10-12", "1996-11-01"]
    for _ in data:
        y, w, d = get_age(datetime.strptime(_, "%Y-%m-%d").date())
        print("{}: {} year, {} weeks, {} days".format(_, y, w, d))


if __name__ == "__main__":
    main()
