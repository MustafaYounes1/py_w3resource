"""

Write a Python program to remove consecutive (following each other continuously) duplicates (elements) from a
given list.


[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]

"""

from itertools import groupby


def main():
    lst = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
    print([_ for _, g in groupby(lst)])


if __name__ == "__main__":
    main()
