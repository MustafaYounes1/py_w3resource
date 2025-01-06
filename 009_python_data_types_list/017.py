"""

Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are
prime otherwise False.

[0, 3, 4, 7, 9] -> False
[3, 5, 7, 13]   -> True
[1, 5, 3]       -> False

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
    lsts = [
        [0, 3, 4, 7, 9],
        [3, 5, 7, 13],
        [1, 5, 3]
    ]

    for _ in lsts:
        print(all(is_prime(__) for __ in _))


if __name__ == "__main__":
    main()
