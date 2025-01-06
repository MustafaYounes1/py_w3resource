"""

Write a Python program to shuffle and print a specified list.

"""

import random


def main():
    random.seed(0)
    lst = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    random.shuffle(lst)
    print(lst)


if __name__ == "__main__":
    main()
