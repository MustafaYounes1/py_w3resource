"""

Write a Python program to insert an element at a specified position into a given list.

[1, 1, 2, 3, 4, 4, 5, 1], 3, 12

[1, 1, 12, 2, 3, 4, 4, 5, 1]

"""


def main():
    lst, idx, el = [1, 1, 2, 3, 4, 4, 5, 1], 3, 12
    lst.insert(idx - 1, el)
    print(lst)


if __name__ == "__main__":
    main()
