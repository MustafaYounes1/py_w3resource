"""

Write a Python program to print the number of prime numbers that are less than or equal to a given number.
Input:
n (1 <= n <= 999,999)
Input the number(n): 35
Number of prime numbers which are less than or equal to n.: 11

"""

from math import sqrt


def is_prime(n):
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False

    return True


def main():
    n = int(input("Enter a number: "))
    res = 0
    while n > 1:
        if is_prime(n):
            res += 1
        n -= 1

    print(res)


if __name__ == "__main__":
    main()
