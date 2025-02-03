"""

Write a Python program to get the dates 30 days before and after today.

Before 30 days: 2025-01-04
Current date:   2025-02-03
After 30 days:  2025-03-05

"""

from datetime import date, timedelta


def main():
    d = date.today()

    print(f"Before 30 days: {d - timedelta(days=30)}")
    print(f"Current date:   {d}")
    print(f"After 30 days:  {d + timedelta(days=30)}")


if __name__ == "__main__":
    main()
