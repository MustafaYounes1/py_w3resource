"""

Write a Python program to generate the running maximum and minimum values of the elements of an iterable.

Running max of [1, 3, 2, 7, 9, 8, 10, 11, 12, 14, 11, 12, 7]
[1, 3, 3, 7, 9, 9, 10, 11, 12, 14, 14, 14, 14]

Running min of [3, 2, 7, 9, 8, 10, 11, 12, 1, 14, 11, 12, 7]
[3, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1]

"""

from itertools import accumulate


def main():
    print(list(accumulate([1, 3, 2, 7, 9, 8, 10, 11, 12, 14, 11, 12, 7], max)))
    print(list(accumulate([3, 2, 7, 9, 8, 10, 11, 12, 1, 14, 11, 12, 7], min)))


if __name__ == "__main__":
    main()
