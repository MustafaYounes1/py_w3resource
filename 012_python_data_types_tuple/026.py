"""

Write a Python program to calculate the product, multiplying all the numbers in a given tuple.

(4, 3, 2, 2, -1, 18)    =>  -864

(2, 4, 8, 8, 3, 2, 9)   =>  27648

"""

from math import prod


def main():
    lst = [
        (4, 3, 2, 2, -1, 18),
        (2, 4, 8, 8, 3, 2, 9)
    ]

    for _ in lst:
        print(prod(_))


if __name__ == "__main__":
    main()
