"""

Write a Python program to find the maximum difference between pairs in a given list.

[32, 14, 90, 10, 22, 42, 31]

(90, 10)

"""

from itertools import combinations
from operator import sub


def main():
    lst = [32, 14, 90, 10, 22, 42, 31]
    print(max(combinations(lst, 2), key=lambda _: abs(sub(*_))))


if __name__ == "__main__":
    main()
