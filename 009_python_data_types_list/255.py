"""

[Starred]

Write a Python program to perform a deep flattening of a list.

[1, [2], [[3], [4], 5], 6]
[1, 2, 3, 4, 5, 6]

[[[1, 2, 3], [4, 5]], 6]
[1, 2, 3, 4, 5, 6]

"""

from collections.abc import Iterable


def deep_flatten(lst):
    if isinstance(lst, Iterable):
        return [__ for _ in lst for __ in deep_flatten(_)]
    else:
        return [lst]


def main():
    data = [
        [1, [2], [[3], [4], 5], 6],
        [[[1, 2, 3], [4, 5]], 6]
    ]

    for lst in data:
        print(deep_flatten(lst))


if __name__ == "__main__":
    main()
