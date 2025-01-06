"""

Write a Python program to calculate the number of days between two dates.

Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days

"""

from datetime import date


def main():
    d1 = date(year=2014, month=7, day=2)
    d2 = date(year=2014, month=7, day=11)
    print(f"{(d2 - d1).days} days")


if __name__ == "__main__":
    main()
