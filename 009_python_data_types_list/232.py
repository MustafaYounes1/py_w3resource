"""

Write a Python program to chunk a given list into smaller lists of a specified size.

[1, 2, 3, 4, 5, 6, 7, 8], 3

[[1, 2, 3], [4, 5, 6], [7, 8]]

"""


def main():
    lst, size = [1, 2, 3, 4, 5, 6, 7, 8], 3
    print([lst[idx: idx + size] for idx in range(0, len(lst), size)])


if __name__ == "__main__":
    main()
