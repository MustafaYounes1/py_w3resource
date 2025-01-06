"""

Write a Python program to remove duplicates from a list of lists.

[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

[[10, 20], [30, 56, 25], [33], [40]]

"""

from itertools import groupby


def main():
    lst = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    print([_ for _, __ in groupby(sorted(lst))])


if __name__ == "__main__":
    main()
