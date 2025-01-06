"""

Write a Python program to flatten a shallow list.

[[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]  =>  [2, 4, 3, 1, 5, 6, 9, 7, 9, 0]

"""
import itertools
from itertools import chain


def main():
    lst = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
    print(list(chain.from_iterable(lst)))
    # or
    # print(list(itertools.chain(*lst)))


if __name__ == "__main__":
    main()
