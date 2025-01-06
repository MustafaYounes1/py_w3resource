"""

Write a Python program to extract common index elements from more than one given list.

[1, 1, 3, 4, 5, 6, 7]
[0, 1, 2, 3, 4, 5, 7]
[0, 1, 2, 3, 4, 5, 7]

[1, 7]

"""


def main():
    data = [
        [1, 1, 3, 4, 5, 6, 7],
        [0, 1, 2, 3, 4, 5, 7],
        [0, 1, 2, 3, 4, 5, 7]
    ]

    print(
        [a for a, b, c in zip(*data) if a == b == c]
    )


if __name__ == "__main__":
    main()
