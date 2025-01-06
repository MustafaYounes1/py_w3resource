"""

Two numbers are coprime if their highest common factor (or greatest common divisor if you must) is 1.
Write a Python program to check if two given numbers are Co Prime or not. Return True if two numbers are Co Prime
otherwise return false.

Sample Input:
(17, 13)    =>  True
(17, 21)    =>  True
(15, 21)    =>  False
(25, 45)    =>  False

"""


def gcd_from_scratch(n1, n2):
    # Use Euclid's algorithm to find the GCD.
    while n2 != 0:
        n1, n2 = n2, n1 % n2

    return n1


def main():
    n1, n2 = [int(_) for _ in input("Enter two space-separated numbers: ").split()]
    print(gcd_from_scratch(n1, n2) == 1)


if __name__ == "__main__":
    main()
