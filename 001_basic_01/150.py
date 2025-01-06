"""

Write a Python function to check whether a distinct pair of numbers whose product is odd is present in a sequence
of integer values.

    [2, 4, 6, 8] False
    [1, 6, 4, 7, 8] True
    [1, 3, 5, 7, 9] True

"""

from itertools import combinations


def check(ll):
    for pair in combinations(ll, 2):
        if (pair[0] * pair[1]) % 2 != 0:
            return True

    return False


def main():
    seq = [int(_) for _ in input("Enter a list of space-separated integers: ").split()]
    print(check(seq))


if __name__ == "__main__":
    main()
