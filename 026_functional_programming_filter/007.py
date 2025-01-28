"""

Write a Python program that filters out prime numbers from a list of integers using the filter function.

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]     =>  [2, 3, 5, 7, 11, 13, 17]

"""

from math import sqrt


def is_prime(n: int) -> bool:
    if n <= 1:
        return False

    for _ in range(2, int(sqrt(n)) + 1):
        if n % _ == 0:
            return False

    return True


def main():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    print(list(filter(is_prime, lst)))


if __name__ == "__main__":
    main()
