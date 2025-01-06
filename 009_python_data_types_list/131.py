"""

Write a Python program to count the frequency of consecutive duplicate elements in a given list of numbers.

[1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5]
([1, 2, 4, 5], [1, 3, 3, 4])


"""

from itertools import groupby


def main():
    lst = [1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5]
    res = [[k, len(list(g))] for k, g in groupby(lst)]
    print([[_[0] for _ in res], [_[1] for _ in res]])


if __name__ == "__main__":
    main()
