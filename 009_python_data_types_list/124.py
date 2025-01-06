"""

Write a Python program to find the maximum and minimum product of pairs of tuples within a given list.

[(2, 7), (2, 6), (1, 8), (4, 9)]
(36, 8)

"""

from math import prod


def main():
    lst = [(2, 7), (2, 6), (1, 8), (4, 9)]
    ps = list(map(prod, lst))
    print(max(ps), min(ps))


if __name__ == "__main__":
    main()
