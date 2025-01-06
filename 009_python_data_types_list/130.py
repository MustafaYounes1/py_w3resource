"""

Write a Python program to count the same pair in three given lists.

[1, 2, 3, 4, 5, 6, 7, 8]
[2, 2, 3, 1, 2, 6, 7, 9]
[2, 1, 3, 1, 2, 6, 7, 9]

3
"""


def main():
    data = [
        [1, 2, 3, 4, 5, 6, 7, 8],
        [2, 2, 3, 1, 2, 6, 7, 9],
        [2, 1, 3, 1, 2, 6, 7, 9]
    ]

    print(len([pair[0] for pair in zip(*data) if len(set(pair)) == 1]))


if __name__ == "__main__":
    main()
