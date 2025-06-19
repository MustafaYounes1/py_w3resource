"""

Write a Python program to implement a generator that generates the Collatz sequence for a given number.

The Collatz sequence, also known as the Collatz conjecture or 3n+1 problem, is a sequence of numbers defined by the
following rules:
    * Start with any positive integer n.
    * If n is even, divide it by 2 to get n/2.
    * If n is odd, multiply it by 3 and add 1 to get 3n+1.
    * Repeat the process, using the resulting number, until you reach the number 1.

For instance, starting with n = 12 and applying the function f without "shortcut", one gets the sequence
    12, 6, 3, 10, 5, 16, 8, 4, 2, 1.

The number n = 19 takes longer to reach 1:
    19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1.

"""

from typing import Generator


def collatz_gen(n: int) -> Generator[int, None, None]:
    curr = n

    while curr > 1:
        yield curr

        if curr % 2 == 0:
            curr //= 2

        else:
            curr = 3 * curr + 1

    yield 1


def main():
    print(list(collatz_gen(12)))
    print(list(collatz_gen(19)))



if __name__ == "__main__":
    main()
