"""

Write a Python program to access multiple elements at a specified index from a given list.

[2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2], [0, 3, 5, 7, 10]
[2, 4, 9, 2, 1]

"""


def main():
    lst, indices = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2], [0, 3, 5, 7, 10]
    print([lst[_] for _ in indices])


if __name__ == "__main__":
    main()
