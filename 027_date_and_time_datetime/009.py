"""

Write a Python program to print the next 5 days starting today.

2025-02-02
2025-02-03
2025-02-04
2025-02-05
2025-02-06
2025-02-07

"""

from datetime import datetime, timedelta


def main():
    curr_d = datetime.now().date()

    for idx in range(6):
        print(curr_d + idx * timedelta(days=1))


if __name__ == "__main__":
    main()
