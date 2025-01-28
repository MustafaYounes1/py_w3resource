"""

Write a Python program to compute the Cartesian product of two or more given lists using itertools.

[1, 2], [3, 4]          =>  [(1, 3), (1, 4), (2, 3), (2, 4)]
[1, 2, 3], [3, 4, 5]    =>  [(1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 3), (3, 4), (3, 5)]
[], [1, 2, 3]           =>  []
[1, 2], []              =>  []

"""

from itertools import product


def main():
    data = [
        [[1, 2], [3, 4]],
        [[1, 2, 3], [3, 4, 5]],
        [[], [1, 2, 3]],
        [[1, 2], []]
    ]

    for _ in data:
        print(list(product(*_)))


if __name__ == "__main__":
    main()
