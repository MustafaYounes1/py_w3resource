"""

Write a Python program to print yesterday, today, tomorrow.

Yesterday:  2025-02-01
Today:      2025-02-02
Tomorrow:   2025-02-03

"""

from datetime import datetime, timedelta


def main():
    td = datetime.now().date()

    print(f"Yesterday:  {td - timedelta(days=1)}")
    print(f"Today:      {td}")
    print(f"Tomorrow:   {td + timedelta(days=1)}")


if __name__ == "__main__":
    main()
