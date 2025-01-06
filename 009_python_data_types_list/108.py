"""

Write a Python program to extract a specified column from a given nested list.

[[1, 2, 3], [2, 4, 5], [1, 1, 1]], 1
[1, 2, 1]

[[1, 2, 3], [-2, 4, -5], [1, -1, 1]], 3
[3, -5, 1]

"""


def main():
    data = [
        [[[1, 2, 3], [2, 4, 5], [1, 1, 1]], 1],
        [[[1, 2, 3], [-2, 4, -5], [1, -1, 1]], 3]
    ]

    for lst, c in data:
        print([lst[i][c - 1] for i in range(len(lst))])


if __name__ == "__main__":
    main()
