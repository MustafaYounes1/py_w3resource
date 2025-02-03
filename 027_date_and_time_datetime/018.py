"""

Write a Python program to get days between two dates.

Sample Dates : 2000,2,28, 2001,2,28
Expected Output : 366 days, 0:00:00

"""

from datetime import datetime


def main():
    s1, s2 = "2000,2,28", "2001,2,28"
    d1, d2 = list(map(lambda _: datetime.strptime(_, "%Y,%m,%d"), (s1, s2)))
    print(max((d1, d2)) - min(d1, d2))


if __name__ == "__main__":
    main()
