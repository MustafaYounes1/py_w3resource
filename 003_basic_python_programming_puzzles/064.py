"""

Write a Python program to find the string consisting of all the words whose lengths are prime numbers.

Input:
The quick brown fox jumps over the lazy dog.
Output:
The quick brown fox jumps the

Input:
Omicron Effect: Foreign Flights Won't Resume On Dec 15, Decision Later.
Output:
Omicron Effect: Foreign Flights Won't On Dec 15,

"""

from math import sqrt


__data = [
    "The quick brown fox jumps over the lazy dog.",
    "Omicron Effect: Foreign Flights Won't Resume On Dec 15, Decision Later."
]


def is_prime(n):
    if n <= 1:
        return False

    for _ in range(2, int(sqrt(n)) + 1):
        if n % _ == 0:
            return False

    return True


def main():
    for sample in __data:
        print(" ".join([_ for _ in sample.split() if is_prime(len(_))]))


if __name__ == "__main__":
    main()
