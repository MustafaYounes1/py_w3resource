"""

Write a Python program to check if a nested list is a subset of another nested list.

[[1, 3], [5, 7], [9, 11], [13, 15, 17]]
[[1, 3], [13, 15, 17]]
True

[[[1, 2], [2, 3]], [[3, 4], [5, 6]]]
[[[3, 4], [5, 6]]]
True

[[[1, 2], [2, 3]], [[3, 4], [5, 7]]]
[[[3, 4], [5, 6]]]
False

"""


def main():
    data = [
        [
            [[1, 3], [5, 7], [9, 11], [13, 15, 17]],
            [[1, 3], [13, 15, 17]]
        ],
        [
            [[[1, 2], [2, 3]], [[3, 4], [5, 6]]],
            [[[3, 4], [5, 6]]]
        ],
        [
            [[[1, 2], [2, 3]], [[3, 4], [5, 7]]],
            [[[3, 4], [5, 6]]]
        ]
    ]

    for lst1, lst2 in data:
        print(all(map(lst1.__contains__, lst2)))


if __name__ == "__main__":
    main()
