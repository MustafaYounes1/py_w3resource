"""

Write a Python program to generate all permutations of a list in Python.

In mathematics, the notion of permutation relates to the act of arranging all the members of a set into some sequence
or order, or if the set is already ordered, rearranging (reordering) its elements, a process called permuting. These
differ from combinations, which are selections of some members of a set where order is disregarded.

[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

"""

from itertools import permutations


def main():
    lst = [1, 2, 3]
    print(list(permutations(lst)))


if __name__ == "__main__":
    main()
