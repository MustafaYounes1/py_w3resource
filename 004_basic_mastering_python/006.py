"""

Convert a list of integers to a list of booleans where all non-zero values become True.

e.g.    [-1, 2, 0, -4, 5]       =>      [True, True, False, True, True]
"""


def main():
    lst = [-1, 2, 0, -4, 5]
    print(list(map(bool, lst)))


if __name__ == "__main__":
    main()
