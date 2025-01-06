"""

Calculate the factorial of a number.

4   =>  24

"""

import math


def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


def main():
    n = 4
    print(math.factorial(n))


if __name__ == "__main__":
    main()
