"""

Write a Python program to unzip a list of tuples into individual lists.

lst = [(1, 2), (3, 4), (8, 9)]

[(1, 3, 8), (2, 4, 9)]

"""


def main():
    lst = [(1, 2), (3, 4), (8, 9)]
    print(list(zip(*lst)))


if __name__ == "__main__":
    main()
