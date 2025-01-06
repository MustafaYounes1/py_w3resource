"""

Find the product of the digits of a number.

12345   =>  120

"""

from math import prod


def main():
    n = 12345
    print(prod(list(map(int, str(n)))))


if __name__ == "__main__":
    main()
