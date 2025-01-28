"""

Write a Python program to add two given lists of different lengths, starting from the left, using the itertools module.

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

    for lst1, lst2 in data:
        print(list(map(sum, zip_longest(lst1, lst2, fillvalue=0))))


if __name__ == "__main__":
    main()
