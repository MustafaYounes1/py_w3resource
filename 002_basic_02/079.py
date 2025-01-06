"""

Write a Python program to compute the largest product of three integers from a given list of integers.

[-10, -20, 20, 1]       =>  4000
[-1, -1, 4, 2, 1]       =>  8
[1, 2, 3, 4, 5, 6]      =>  120

"""

from itertools import combinations
from math import prod
from sys import maxsize


def main():
    seq = list(map(int, input("Enter a list of space-separated integers: ").split()))

    p = -maxsize
    for comb in combinations(seq, 3):
        _ = prod(comb)
        if _ > p:
            p = _

    print(p)


if __name__ == "__main__":
    main()
