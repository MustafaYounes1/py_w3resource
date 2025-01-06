"""

Write a Python program to compute the sum of non-zero groups (separated by zeros) of a given list of numbers.

[3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1, 0, 0, 0]

[15, 38, 15, 27]

"""

from itertools import groupby


def main():
    lst = [
        3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1,
        0, 0, 0
    ]

    res = []
    s = 0
    for k, g in groupby(lst):
        if k != 0:
            s += k * len(list(g))
        else:
            if s:
                res.append(s)
            s = 0

    print(res)


if __name__ == "__main__":
    main()
