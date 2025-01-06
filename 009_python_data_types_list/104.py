"""

Write a Python program to find the difference between consecutive numbers in a given list.

[1, 1, 3, 4, 4, 5, 6, 7]
[0, 2, 1, 0, 1, 1, 1]

[4, 5, 8, 9, 6, 10]
[1, 3, 1, -3, 4]

"""


def main():
    data = [
        [1, 1, 3, 4, 4, 5, 6, 7],
        [4, 5, 8, 9, 6, 10]
    ]

    for ll in data:
        print([b - a for a, b in zip(ll[:-1], ll[1:])])


if __name__ == "__main__":
    main()
