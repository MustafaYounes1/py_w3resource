"""

Write a Python program to convert a given list of tuples to a list of lists.

[(1, 2), (2, 3), (3, 4)]
[[1, 2], [2, 3], [3, 4]]

[(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
[[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]

"""


def main():
    data = [
        [(1, 2), (2, 3), (3, 4)],
        [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
    ]

    for _ in data:
        print(list(map(list, _)))


if __name__ == "__main__":
    main()
