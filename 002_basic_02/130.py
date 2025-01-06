"""

Write a Python program to check whether a given month and year contains a Monday 13th.

Month No.: 11 Year: 2022       =>   False
Month No.: 6 Year: 2022        =>   True

"""

from datetime import date


def main():
    month, year = [int(_) for _ in input("Enter the month and year (space-separated): ").split()]
    print(date(year=year, month=month, day=13).strftime("%A") == "Monday")


if __name__ == "__main__":
    main()
