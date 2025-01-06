"""

Write a Python program to compute the average of the n-th element in a given list of lists with different lengths.

[[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
[4.8, 5.8, 6.8, 8.0, 11.0]

"""

from itertools import zip_longest
from statistics import mean


def main():
    lst = [[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
    print(list(map(lambda _: mean([__ for __ in _ if __ is not None]), zip_longest(*lst, fillvalue=None))))


if __name__ == "__main__":
    main()
