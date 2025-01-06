"""

Given a list of numbers and a number k, write a Python program to check whether the sum of any two numbers from the
list is equal to k or not.

For example, given [1, 5, 11, 5] and k = 16, return true since 11 + 5 is 16.

Sample Input:
([12, 5, 0, 5], 10)     => True
([20, 20, 4, 5], 40)    => True
([1, -1], 0)            => True
([1, 1, 0], 0)          => False

"""

from itertools import combinations
import sys


def main():
    seq = [int(_) for _ in input("Enter a list of space-separated integers: ").split()]
    n = int(input("Enter the number: "))

    for comb in combinations(seq, 2):
        if sum(comb) == n:
            print(True)
            sys.exit(0)

    print(False)


if __name__ == "__main__":
    main()
