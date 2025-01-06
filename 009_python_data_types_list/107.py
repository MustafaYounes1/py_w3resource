"""

Write a Python program to remove a specified column from a given nested list.

[[1, 2, 3], [2, 4, 5], [1, 1, 1]], 1
[[2, 3], [4, 5], [1, 1]]

[[1, 2, 3], [-2, 4, -5], [1, -1, 1]], 3
[[1, 2], [-2, 4], [1, -1]]

"""


def main():
    data = [
        [[[1, 2, 3], [2, 4, 5], [1, 1, 1]], 1],
        [[[1, 2, 3], [-2, 4, -5], [1, -1, 1]], 3]
    ]

    for lst, c in data:
        print([[__ for idx, __ in enumerate(_) if idx != (c - 1)] for _ in lst])


if __name__ == "__main__":
    main()
