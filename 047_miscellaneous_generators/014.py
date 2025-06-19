"""

Write a Python program to implement a generator that generates the next Armstrong number after a given number.

Armstrong numbers, also known as narcissistic numbers, are numbers that are equal to the sum of their digits each raised
to the power of the number of digits.

For example 153 is an Armstrong number because 153 = 1^3+5^3+3^3.

370     =>  371
153     =>  370
407     =>  1634

"""

from typing import Generator


def is_armstrong(n: int) -> bool:
    s = str(n)
    return n == sum(int(d) ** len(s) for d in s)


def armstrong_gen() -> Generator[int, None, None]:
    """Infinite armstrong number generators"""
    i = 0

    while True:
        if is_armstrong(i):
            tmp = yield i

            if tmp is not None:
                i = tmp

        i += 1


def get_next_armstrong(n: int) -> int:
    """get the armstrong number that follows n"""
    gen = armstrong_gen()
    next(gen)  # .send should be called after starting the generator (.send resumes starting from the last yield)
    return gen.send(n)


def main():
    data = [370, 153, 407]

    for _ in data:
        print(get_next_armstrong(_))


if __name__ == "__main__":
    main()
