"""

Write a Python program to subtract five days from the current date.

Current Date:               2025-02-02
5 days before Current Date: 2025-01-28

"""

from datetime import datetime, timedelta


def main():
    curr_d = datetime.now().date()

    print(f"Current Date:               {curr_d}")
    print(f"5 days before Current Date: {curr_d - timedelta(days=5)}")


if __name__ == "__main__":
    main()
