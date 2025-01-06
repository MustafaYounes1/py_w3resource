"""

Get the common items between two lists.

    lst1 = [1, 2, 3, 4, 5]
    lst2 = [3, 4, 5, 6, 7]

    [3, 4, 5]

"""


def main():
    lst1 = [1, 2, 3, 4, 5]
    lst2 = [3, 4, 5, 6, 7]
    print(list(set(lst1) & set(lst2)))


if __name__ == "__main__":
    main()
