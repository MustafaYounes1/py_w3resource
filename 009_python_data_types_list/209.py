"""

Write a Python program to count the number of groups of non-zero numbers separated by zeros in a given list of numbers.

[3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 5, 9, 9, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1]
4

"""

from itertools import groupby


def main():
    lst = [
        3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 5, 9, 9, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7,
        1
    ]

    new_group = True

    count = 0
    for k, g in groupby(lst):
        if k != 0 and new_group:
            count += 1
            new_group = False

        elif k == 0:
            new_group = True

    print(count)


if __name__ == "__main__":
    main()
