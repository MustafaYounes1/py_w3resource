"""

Write a Python program to interleave a number of lists of different lengths using the itertools module.

[2, 4, 7, 0, 5, 8]
[2, 5, 8]
[0, 1]
[3, 3, -1, 7]

[2, 2, 0, 3, 4, 5, 1, 3, 7, 8, -1, 0, 7, 5, 8]

"""

from itertools import chain, zip_longest


def main():
    lst1 = [2, 4, 7, 0, 5, 8]
    lst2 = [2, 5, 8]
    lst3 = [0, 1]
    lst4 = [3, 3, -1, 7]

    print([_ for _ in chain.from_iterable(zip_longest(lst1, lst2, lst3, lst4)) if _ is not None])


if __name__ == "__main__":
    main()
