"""

Write a Python program to find the greatest common divisor (GCD) of two integers using recursion.

48, 12      =>  12

"""


def gcd(n1, n2):
    low, high = min(n1, n2), max(n1, n2)

    if not low:
        return high

    elif low == 1:
        return 1

    else:
        return gcd(low, high % low)


def main():
    n1, n2 = 48, 12
    print(gcd(n1, n2))


if __name__ == "__main__":
    main()
