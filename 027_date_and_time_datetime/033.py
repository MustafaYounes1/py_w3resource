"""

Write a Python program to calculate the number of days between two date times.

2016/10/12 00:00:00, 2015/12/10 00:00:00    =>  307
2016/10/12 00:00:00, 2015/12/10 23:59:59    =>  306

"""

from datetime import datetime


def main():
    data = [
        ("2016/10/12 00:00:00", "2015/12/10 00:00:00"),
        ("2016/10/12 00:00:00", "2015/12/10 23:59:59")
    ]

    for s1, s2 in data:
        d1, d2 = map(lambda _: datetime.strptime(_, "%Y/%m/%d %H:%M:%S"), (s1, s2))
        print((max(d1, d2) - min(d1, d2)).days)

if __name__ == "__main__":
    main()
