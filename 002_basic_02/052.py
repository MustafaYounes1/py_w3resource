"""

Write a Python program to compute the sum of the first n prime numbers.

Input:
n ( n <= 10000). Input 0 to exit the program.
Input a number (n<=10000) to compute the sum:(0 to exit)    25
Sum of first 25 prime numbers:                              1060

"""

from math import sqrt


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def main():
    n = int(input("Enter the number: "))
    s, num, i = 0, 2, 0

    while i < n:
        if is_prime(num):
            s += num
            i += 1

        num += 1

    print(s)


if __name__ == "__main__":
    main()
