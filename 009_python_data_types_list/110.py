"""

Write a Python program to find the item with the most occurrences in a given list.

[2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
2

"""


def main():
    lst = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
    print(max(lst, key=lst.count))


if __name__ == "__main__":
    main()
