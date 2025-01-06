"""

Write a Python program to find the difference between elements (n+1th - nth) of a given list of numeric values.

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 1, 1, 1, 1, 1, 1, 1, 1]

[2, 4, 6, 8]
[2, 2, 2]

"""


def main():
    data = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [2, 4, 6, 8]
    ]

    for _ in data:
        print([b - a for a, b in zip(_[:-1], _[1:])])


if __name__ == "__main__":
    main()
