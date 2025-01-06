"""

Write a Python program to randomize the order of the values of a list, returning a new list.

[1, 2, 3, 4, 5, 6]

"""

import random


def main():
    random.seed(0)

    lst = [1, 2, 3, 4, 5, 6]
    random.shuffle(lst)

    print(lst)


if __name__ == "__main__":
    main()
