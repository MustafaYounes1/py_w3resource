"""

Write a Python function that finds all the permutations of the members of a list.

In mathematics, the notion of permutation relates to the act of arranging all the members of a set into some sequence
or order, or if the set is already ordered, rearranging (reordering) its elements, a process called permuting. These
differ from combinations, which are selections of some members of a set where order is disregarded

[1, 2, 3, 4]    =>  [
    [1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2], [2, 1, 3, 4], [2, 1, 4, 3],
    [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1], [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1],
    [3, 4, 1, 2], [3, 4, 2, 1], [4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]
]

[-100, -300, 0] =>  [
    [-100, -300, 0], [-100, 0, -300], [-300, -100, 0], [-300, 0, -100], [0, -100, -300], [0, -300, -100]
]

"""

from itertools import permutations


def main():
    data = [
        [1, 2, 3, 4],
        [-100, -300, 0]
    ]

    for lst in data:
        print(list(permutations(lst, len(lst))))


if __name__ == "__main__":
    main()
