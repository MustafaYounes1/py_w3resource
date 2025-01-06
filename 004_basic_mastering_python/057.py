"""

Find the intersection of two lists.

lst1 = [1, 2, 3, 4]
lst2 = [3, 4, 5, 6]

[3, 4]

"""


def main():
    lst1 = [1, 2, 3, 4]
    lst2 = [3, 4, 5, 6]
    print(list(set(lst1) & set(lst2)))


if __name__ == "__main__":
    main()
