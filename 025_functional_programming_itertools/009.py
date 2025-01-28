"""

Write a Python program to create an iterator to get a specified number of permutations of elements.

['A', 'B', 'C', 'D'], 3

[
    ('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'B'), ('A', 'C', 'D'), ('A', 'D', 'B'), ('A', 'D', 'C'),
    ('B', 'A', 'C'), ('B', 'A', 'D'), ('B', 'C', 'A'), ('B', 'C', 'D'), ('B', 'D', 'A'), ('B', 'D', 'C'),
    ('C', 'A', 'B'), ('C', 'A', 'D'), ('C', 'B', 'A'), ('C', 'B', 'D'), ('C', 'D', 'A'), ('C', 'D', 'B'),
    ('D', 'A', 'B'), ('D', 'A', 'C'), ('D', 'B', 'A'), ('D', 'B', 'C'), ('D', 'C', 'A'), ('D', 'C', 'B')
]

"""

from itertools import permutations


def main():
    lst = ['A', 'B', 'C', 'D']
    print(list(permutations(lst, 3)))


if __name__ == "__main__":
    main()
