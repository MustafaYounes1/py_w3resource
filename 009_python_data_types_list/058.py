"""

Write a Python program to replace the last element in a list with another list.

[1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
[1, 3, 5, 7, 9, 2, 4, 6, 8]

"""


def main():
    lst1, lst2 = [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
    print(lst1[:-1] + lst2)


if __name__ == "__main__":
    main()
