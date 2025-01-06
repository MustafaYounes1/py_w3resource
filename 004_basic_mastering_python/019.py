"""

Calculate the dot product of two lists.

    lst1 = [1, 2, 3]
    lst2 = [4, 5, 6]

    32

"""


def main():
    lst1 = [1, 2, 3]
    lst2 = [4, 5, 6]
    print(sum([i * j for i, j in zip(lst1, lst2)]))


if __name__ == "__main__":
    main()
