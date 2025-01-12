"""

Write a Python program to find the two numbers whose product is maximum among all the pairs in a given list of numbers.
Note: Use the Python set.

[1, 2, 3, 4, 5, 6, 7, 8, 9]         =>  (8, 9)
[1, -2, -3, 4, 5, -6, 7, -8, 9]     =>  (7, 9)

"""

from itertools import combinations
from math import prod


def main():
    data = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, -2, -3, 4, 5, -6, 7, -8, 9]
    ]

    for lst in data:
        print(
            tuple(max(set(map(frozenset, combinations(lst, 2))), key=prod))
        )


if __name__ == "__main__":
    main()
