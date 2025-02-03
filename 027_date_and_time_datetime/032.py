"""

Write a Python program to calculate the number of days between two dates.

2016/10/12, 2015/12/10  =>  307
2016/3/23, 2017/12/10   =>  627

"""

from datetime import datetime


def main():
    data = [
        ("2016/10/12", "2015/12/10"),
        ("2016/3/23", "2017/12/10")
    ]

    for s1, s2 in data:
        d1, d2 = map(lambda _: datetime.strptime(_, "%Y/%m/%d"), (s1, s2))
        print((max(d1, d2) - min(d1, d2)).days)


if __name__ == "__main__":
    main()
