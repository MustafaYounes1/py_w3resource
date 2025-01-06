"""

Write a Python program to add two given lists of different lengths, starting on the right.

[2, 4, 7, 0, 5, 8]
[3, 3, -1, 7]

[2, 4, 10, 3, 4, 15]

[1, 2, 3, 4, 5, 6]
[2, 4, -3]

[1, 2, 3, 6, 9, 3]

"""


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
        ma = max(len(l1), len(l2))
        print(
            [
                sum([_, __]) for _, __ in zip([0] * abs(len(l1) - ma) + l1, [0] * abs(len(l2) - ma) + l2)
            ]
        )


if __name__ == "__main__":
    main()
