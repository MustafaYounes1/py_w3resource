"""

Write a Python program to select the odd items from a list.

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

[1, 3, 5, 7, 9]

"""


def main():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print([_ for _ in lst if _ % 2 != 0])


if __name__ == "__main__":
    main()
