"""

Write a Python program to create a list reflecting the modified run-length encoding from a given list of integers or
a given list of characters.

[1, 1, 2, 3, 4, 4, 5, 1]
[[2, 1], 2, 3, [2, 4], 5, 1]

aabcddddadnss
[[2, 'a'], 'b', 'c', [4, 'd'], 'a', 'd', 'n', [2, 's']]

"""

from itertools import groupby


def parse_group(g):
    if len(g) > 1:
        return [len(g), g[0]]
    else:
        return g[0]


def main():
    data = [
        [1, 1, 2, 3, 4, 4, 5, 1],
        'aabcddddadnss'
    ]

    for _ in data:
        print([parse_group(list(g)) for k, g in groupby(_)])


if __name__ == "__main__":
    main()
