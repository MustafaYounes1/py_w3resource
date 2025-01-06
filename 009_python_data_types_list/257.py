"""

Write a Python program to check if two given lists contain the same elements regardless of order.

[1, 2, 4]
[2, 4, 1]
True

[1, 2, 3]
[1, 2, 3]
True

[1, 2, 3]
[1, 2, 4]
False

"""


def main():
    data = [
        [
            [1, 2, 4],
            [2, 4, 1]
        ],
        [
            [1, 2, 3],
            [1, 2, 3]
        ],
        [
            [1, 2, 3],
            [1, 2, 4]
        ]
    ]

    for lst1, lst2 in data:
        print(set(lst1) == set(lst2))


if __name__ == "__main__":
    main()
