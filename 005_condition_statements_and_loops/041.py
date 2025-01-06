"""

Write a Python program to get the next day of a given date.
Expected Output:

Input a year: 2016
Input a month [1-12]: 08
Input a day [1-31]: 23
The next date is [yyyy-mm-dd] 2016-8-24

"""

from datetime import date, timedelta


def main():
    y, m, d = list(map(int, input("Enter year, month, day white-separated as integers: ").split()))
    print(date(year=y, month=m, day=d) + timedelta(days=1))

if __name__ == "__main__":
    main()
