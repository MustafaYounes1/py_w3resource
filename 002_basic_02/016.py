"""

Write a Python program to get the third side of a right-angled triangle from two given sides.

"""

from math import sqrt


def main():
    a, b = [int(_) for _ in input("Enter the two sides space-separated: ").split()]
    print(f"{sqrt(pow(a, 2) + pow(b, 2)):.2f}")


if __name__ == "__main__":
    main()
