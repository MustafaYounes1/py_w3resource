"""

Write a Python program to add two given lists of different lengths, starting on the left.

[2, 4, 7, 0, 5, 8]
[3, 3, -1, 7]

[5, 7, 6, 7, 5, 8]

[1, 2, 3, 4, 5, 6]
[2, 4, -3]

[3, 6, 0, 4, 5, 6]

"""

from itertools import zip_longest


def main():
    data = [
        [
            [2, 4, 7, 0, 5, 8],
            [3, 3, -1, 7]
        ],
        [
            [1, 2, 3, 4, 5, 6],
            [2, 4, -3]
        ]
    ]

    for l1, l2 in data:
        print([sum(_) for _ in zip_longest(l1, l2, fillvalue=0)])


if __name__ == "__main__":
    main()
