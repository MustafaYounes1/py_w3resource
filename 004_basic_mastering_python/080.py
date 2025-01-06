"""

Find the least common multiple (LCM) of two numbers.

4, 5    =>  20

"""

import math


def lcm(a, b):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    return a * b // gcd(a, b)


def main():
    n1, n2 = 4, 5
    print(math.lcm(n1, n2))


if __name__ == "__main__":
    main()
