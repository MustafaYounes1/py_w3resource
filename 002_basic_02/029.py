"""

Write a Python program to find the greatest common divisor between two numbers in a given pair. (GCD)

    2, 4        =>  2
    2, 8        =>  2
    336, 360    =>  24

"""

from math import gcd


def main():
    a, b = [int(_) for _ in input("Enter two space-separated numbers: ").split()]
    print(gcd(a, b))


if __name__ == "__main__":
    main()
