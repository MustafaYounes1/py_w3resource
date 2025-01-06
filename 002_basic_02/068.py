"""

Write a Python program that counts the number of prime numbers that are less than a given non-negative number.
Sample Input:
(10)    =>  4
(100)   =>  25

"""

from math import sqrt


def is_prime(n):
    for _ in range(2, int(sqrt(n)) + 1):
        if n % _ == 0:
            return False

    return True


def main():
    n = int(input("Enter a number: "))
    res = [_ for _ in range(2, n) if is_prime(_)]
    print(len(res))


if __name__ == "__main__":
    main()
