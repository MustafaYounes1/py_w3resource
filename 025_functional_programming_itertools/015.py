"""

Write a Python program to find the sorted sequence from a set of permutations of a given input.
    Note: find the sorted sequences in ascending order

[12, 10, 9]     =>  [(9, 10, 12)]
[2, 3, 1, 0]    =>  [(0, 1, 2, 3)]

"""

from itertools import pairwise, permutations


def main():
    data = [
        [12, 10, 9],
        [2, 3, 1, 0]
    ]

    for _ in data:
        print(list(filter(lambda __: all(b > a for a, b in pairwise(__)), permutations(_))))


if __name__ == "__main__":
    main()
