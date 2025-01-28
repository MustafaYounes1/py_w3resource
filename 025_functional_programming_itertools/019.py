"""

Write a Python program to find the factorial of a number using the itertools module.

5   =>  120

"""

from itertools import count, islice
from math import prod


def main():
    n = 5
    print(prod(islice(count(1), n)))


if __name__ == "__main__":
    main()
