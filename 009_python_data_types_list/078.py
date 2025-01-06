"""

Write a Python program to split a given list into two parts where the length of the first part of the list is given.

[1, 1, 2, 3, 4, 4, 5, 1], 3

([1, 1, 2], [3, 4, 4, 5, 1])

"""


def main():
    lst, l = [1, 1, 2, 3, 4, 4, 5, 1], 3
    print([lst[0:l], lst[l:]])


if __name__ == "__main__":
    main()
