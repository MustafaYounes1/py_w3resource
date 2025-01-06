"""

Write a Python program to select an item randomly from a list.

['Red', 'Blue', 'Green', 'White', 'Black']      =>    White

"""

import random


def main():
    random.seed(0)
    lst = ['Red', 'Blue', 'Green', 'White', 'Black']
    print(random.choice(lst))


if __name__ == "__main__":
    main()
