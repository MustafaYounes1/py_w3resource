"""

Write a Python program to count the frequency of consecutive duplicate elements in a given list of numbers.
Use the itertools module.

[1, 1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5]    =>  [2, 3, 3, 4]

"""

from itertools import groupby


def main():
    lst = [1, 1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5]
    print([len(list(g)) for _, g in groupby(lst)])


if __name__ == "__main__":
    main()
