"""

Write a Python program to calculate the difference between two dates in seconds.

2015-01-01 01:00:00, 2015-05-27 14:04:03    =>  12661443.0

"""

from datetime import datetime


def main():
    s1, s2 = "2015-01-01 01:00:00", "2015-05-27 14:04:03"
    d1, d2 = map(lambda _: datetime.strptime(_, "%Y-%m-%d %H:%M:%S"), (s1, s2))
    print((max(d1, d2) - min(d1, d2)).total_seconds())


if __name__ == "__main__":
    main()
