"""

Write a Python program to compute prime numbers up to a specified number.

100
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

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
    n = 100
    print(
        [_ for _ in range(2, n + 1) if is_prime(_)]
    )


if __name__ == "__main__":
    main()
