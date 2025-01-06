"""

Write a Python program to get the powerset of a given iterable.

[1, 2]
[(), (1,), (2,), (1, 2)]

[1, 2, 3, 4]
[
    (), (1,), (2,), (3,), (4,), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4), (1, 2, 3), (1, 2, 4), (1, 3, 4),
    (2, 3, 4), (1, 2, 3, 4)
]

"""

from itertools import combinations


def main():
    data = [
        [1, 2],
        [1, 2, 3, 4]
    ]

    for lst in data:
        print([__ for size in range(len(lst) + 1) for __ in combinations(lst, size)])


if __name__ == "__main__":
    main()
