"""

Find the greatest common divisor (GCD) of two numbers.

48, 18  =>  6

"""

from math import gcd


def gcd_from_scratch(a, b):
    while b:
        a, b = b, a % b

    return a


def main():
    n1, n2 = 48, 18
    print(gcd(n1, n2))


if __name__ == "__main__":
    main()
