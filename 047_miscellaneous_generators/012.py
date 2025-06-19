"""

Write a Python program to implement a generator that generates the next happy number after a given number.

From Wikipedia: In number theory, a happy number is a number which eventually reaches 1 when replaced by the sum of the
square of each digit. For instance, 13 is a happy number because 1^2 + 3^2 = 10 and 1^2 + o^2 = 1

On the other hand, 4 is not a happy number because the sequence starting with 4^2 = 16 and 1^2 + 6^2 = 37 eventually
reaches 2^2 + 0^2 =4, the number that started the sequence, and so the process continues in an infinite cycle without
ever reaching 1. A number which is not happy is called sad or unhappy.

The first 20 happy numbers are 1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100, ...

"""

from itertools import islice
from typing import Generator


def is_happy(n: int) -> bool:
    curr, seen = n, set()

    while True:
        curr = sum(int(d) ** 2 for d in str(curr))

        if curr == 1:
            return True

        elif curr in seen:
            return False

        seen.add(curr)


def happy_numbers() -> Generator[int, None, None]:
    i = 1

    while True:
        if is_happy(i):
            yield i

        i += 1


def main():
    print(list(islice(happy_numbers(), 20)))


if __name__ == "__main__":
    main()
