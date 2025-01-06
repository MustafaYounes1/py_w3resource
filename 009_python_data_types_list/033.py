"""

Write a Python program to generate all sub-lists of a list.

['X', 'Y', 'Z']
[(), ('X',), ('Y',), ('Z',), ('X', 'Y'), ('X', 'Z'), ('Y', 'Z'), ('X', 'Y', 'Z')]

"""

from itertools import combinations


def main():
    lst = ['X', 'Y', 'Z']
    res = []

    for _ in range(len(lst) + 1):
        res += list(combinations(lst, _))

    print(res)


if __name__ == "__main__":
    main()
