"""

Write a Python program to find all the unique combinations of 3 numbers from a given list of numbers, adding up to
a target number. Note: try to use Python sets

[1, 2, 3, 4, 5, 6, 7, 8, 9]

12      =>  [(1, 3, 8), (1, 4, 7), (1, 2, 9), (1, 5, 6), (3, 4, 5), (2, 3, 7), (2, 4, 6)]
17      =>  [(4, 5, 8), (2, 6, 9), (3, 5, 9), (2, 7, 8), (4, 6, 7), (3, 6, 8), (1, 7, 9)]

"""

from itertools import combinations


def main():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sums = (12, 17)

    uniq_combs = set(map(frozenset, combinations(lst, 3)))
    for s in sums:
        print(list(filter(lambda _: sum(_) == s, uniq_combs)))


if __name__ == "__main__":
    main()
