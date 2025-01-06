"""

Write a Python program to identify non-prime numbers between 1 and 100 (integers). Print the non-prime numbers.

Sample Input:
range(1, 101)

Sample Output:
Nonprime numbers between 1 to 100:
4
6
8
9
10
..
96
98
99
100

"""

from math import sqrt


def is_prime(n):
    for _ in range(2, int(sqrt(n)) + 1):
        if n % _ == 0:
            return False

    return True


def main():
    for _ in range(1, 101):
        if not is_prime(_):
            print(_)


if __name__ == "__main__":
    main()
