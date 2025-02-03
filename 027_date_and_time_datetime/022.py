"""

Write a Python program to get the number of days in a given month and year.

2025,  1, 31
2025,  2, 28
2025,  3, 31
2025,  4, 30
2025,  5, 31
2025,  6, 30
2025,  7, 31
2025,  8, 31
2025,  9, 30
2025, 10, 31
2025, 11, 30
2025, 12, 31

"""

from datetime import date


def month_days(y: int, m: int) -> int:
    assert m in range(1, 13), "Invalid month, should fall in the range [1, 12]"
    yy, mm = y + m // 12, m % 12 + 1
    return (date(year=yy, month=mm, day=1) - date(year=y, month=m, day=1)).days


def main():
    y = 2025
    for _ in range(1, 13):
        print(f"{y:4d}, {_:2d}, {month_days(y, _):2d}")


if __name__ == "__main__":
    main()
