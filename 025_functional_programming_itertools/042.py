"""

Write a Python program to extract a non-zero block from a given integer list.

[3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1]

[[3, 4, 6, 2], [6, 7, 6, 9, 10], [7, 4, 4], [5, 3, 2, 9, 7, 1]]

"""

from itertools import groupby


def main():
    lst = [3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1]
    print([list(g) for k, g in groupby(lst, lambda _: bool(_)) if k])


if __name__ == "__main__":
    main()
