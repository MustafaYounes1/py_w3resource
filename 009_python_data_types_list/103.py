"""

Write a Python program to extract specified number of elements from a given list, which follows each other continuously.

[1, 1, 3, 4, 4, 5, 6, 7], 2
[1, 4]

[0, 1, 2, 3, 4, 4, 4, 4, 5, 7], 4
[4]

"""

from itertools import groupby


def main():
    data = [
        [[1, 1, 3, 4, 4, 5, 6, 7], 2],
        [[0, 1, 2, 3, 4, 4, 4, 4, 5, 7], 4]
    ]

    for lst, ll in data:
        print([k for k, g in groupby(lst) if len(list(g)) == ll])


if __name__ == "__main__":
    main()
