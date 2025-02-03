"""

Write a Python program to convert difference of two dates into days, hours, minutes, and seconds.

2015-01-01 01:15:02, 2015-02-04 03:04:03    =>  34 days, 1 hours, 49 minutes, 1 sec

"""

from datetime import datetime


def main():
    s1, s2 = "2015-01-01 01:15:02", "2015-02-04 03:04:03"
    d1, d2 = map(lambda _: datetime.strptime(_, "%Y-%m-%d %H:%M:%S"), (s1, s2))
    td = max(d1, d2) - min(d1, d2)

    m, s = divmod(td.seconds, 60)
    h, m = divmod(m, 60)
    print(f"{td.days} days, {h} hours, {m} minutes, {s} sec")


if __name__ == "__main__":
    main()
