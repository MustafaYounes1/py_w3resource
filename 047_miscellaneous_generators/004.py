"""

Write a Python program to implement a generator function that generates the Fibonacci sequence.

first 20 fib numbers: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

"""

from typing import Generator


def fib_gen() -> Generator[int, None, None]:
    a, b = 0, 1

    yield a
    yield b

    while True:
        a, b = b, a + b
        yield b


def main():
    gen = fib_gen()
    print([next(gen) for _ in range(20)])


if __name__ == "__main__":
    main()
