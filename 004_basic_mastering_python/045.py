"""

Calculate the element-wise square of the difference between two lists.

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

[9, 9, 9]

"""


def main():
    lst1 = [1, 2, 3]
    lst2 = [4, 5, 6]
    print([pow(i - j, 2) for i, j in zip(lst1, lst2)])


if __name__ == "__main__":
    main()
