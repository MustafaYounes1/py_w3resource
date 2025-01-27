"""

Write a Python program to calculate the product of a given list of numbers using lambda.

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]     =>  3628800
[2.2, 4.12, 6.6, 8.1, 8.3]          =>  4021.8599520000007
[4, 3, 2, 2, -1, 18]                =>  -864
[2, 4, 8, 8, 3, 2, 9]               =>  -27648

"""

from functools import reduce


def main():
    data = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [2.2, 4.12, 6.6, 8.1, 8.3],
        [4, 3, 2, 2, -1, 18],
        [2, 4, 8, 8, 3, 2, 9]
    ]

    for lst in data:
        print(reduce(lambda a, b: a * b, lst, 1))


if __name__ == "__main__":
    main()
