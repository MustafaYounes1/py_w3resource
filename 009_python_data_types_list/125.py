"""

Write a Python program to calculate the product of the unique numbers in a given list.

Original List : [10, 20, 30, 40, 20, 50, 60, 40]
Product of the unique numbers of the said list: 720,000,000

"""

from math import prod


def main():
    lst = [10, 20, 30, 40, 20, 50, 60, 40]
    print("{:,}".format(prod(set(lst))))


if __name__ == "__main__":
    main()
