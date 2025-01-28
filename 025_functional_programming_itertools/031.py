"""

Write a Python program to find pairs of maximum and minimum products from a given list. Use the itertools module.

[2, 5, 8, 7, 4, 3, 1, 9, 10, 1]

Pairs of maximum and minimum product from the said list:
((9, 10), (1, 1))

"""

from itertools import combinations
from math import prod


def main():
    lst = [2, 5, 8, 7, 4, 3, 1, 9, 10, 1]
    combs = list(combinations(lst, 2))
    print(max(combs, key=prod))
    print(min(combs, key=prod))


if __name__ == "__main__":
    main()
