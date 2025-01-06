"""

Write a Python program to find which characters of a hexadecimal number correspond to prime numbers.

Input: 123ABCD
Output:
[False, True, True, False, True, False, True]

Input: 123456
Output:
[False, True, True, False, True, False]

Input: FACE
Output:
[False, False, False, False]

"""

from math import sqrt


def is_prime(n):
    if n <= 1:
        return False

    for _ in range(2, int(sqrt(n)) + 1):
        if n % _ == 0:
            return False

    return True


def main():
    n = input("Enter a number: ")
    print(
        [is_prime(int(_, 16)) for _ in n]
    )


if __name__ == "__main__":
    main()
