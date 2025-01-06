"""

Write a Python program to remove the K'th element from a given list, and print the updated list.

[1, 1, 2, 3, 4, 4, 5, 1], 3

[1, 1, 3, 4, 4, 5, 1]

"""


def main():
    lst, idx = [1, 1, 2, 3, 4, 4, 5, 1], 3
    lst.pop(idx - 1)
    print(lst)


if __name__ == "__main__":
    main()
