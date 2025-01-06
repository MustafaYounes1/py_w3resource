"""

Write a Python program to swap two sublists in a given list.

[[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15]]

[[0, 1, 2, 3, 4], [10, 11, 12, 13, 14, 15], [5, 6, 7, 8, 9]]

"""


def main():
    lst = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15]]
    lst[1], lst[2] = lst[2], lst[1]
    print(lst)


if __name__ == "__main__":
    main()
