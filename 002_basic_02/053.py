"""

Write a Python program which accepts an even number (>=4, Goldbach number) from the user and creates combinations
which express the given number as a sum of two prime numbers. Print the number of combinations.

Goldbach number: A Goldbach number is a positive even integer that can be expressed as the sum of two odd primes.
Since four is the only even number greater than two that requires the even prime 2 in order to be written as the sum
of two primes, another form of the statement of Goldbach's conjecture is that all even integers greater than 4 are
Goldbach numbers.

The expression of a given even number as a sum of two primes is called a Goldbach partition of that number.
The following are examples of Goldbach partitions for some even numbers:
6 = 3 + 3
8 = 3 + 5
10 = 3 + 7 = 5 + 5
12 = 7 + 5
...
100 = 3 + 97 = 11 + 89 = 17 + 83 = 29 + 71 = 41 + 59 = 47 + 53

Input an even number (0 to exit):   100
Number of combinations:             6

"""

from itertools import combinations
from math import sqrt

def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def find_odd_primes_less_than(n):
    res = []
    for i in range(3, n, 2):
        if is_prime(i):
            res.append(i)

    return res


def main():
    n = int(input("Input an even number >= 4: "))
    assert n >= 4, "Invalid input"

    n_valid_comb = 0
    for comb in combinations(find_odd_primes_less_than(n), 2):
        if sum(comb) == n:
            n_valid_comb += 1

    print(n_valid_comb)


if __name__ == "__main__":
    main()
