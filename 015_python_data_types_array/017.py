"""

Write a Python program to find a pair with the highest product from a given array of signed integers.

[1, 2, 3, 4, 7, 0, 8, 4]    =>  (8, 7)
[0, -1, -2, -4, 5, 0, -6]   =>  (-6, -4)

"""

from array import array
from itertools import combinations
from math import prod


def main():
    data = [
        array('i', [1, 2, 3, 4, 7, 0, 8, 4]),
        array('i', [0, -1, -2, -4, 5, 0, -6])
    ]

    for arr in data:
        print(tuple(max(map(set, combinations(arr, 2)), key=prod)))


if __name__ == "__main__":
    main()
