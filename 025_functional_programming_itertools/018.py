"""

Write a Python program that iterates the integers from 1 to a given number and prints "Fizz" for multiples of three,
prints "Buzz" for multiples of five, and prints "FizzBuzz" for multiples of both three and five using the itertools
module.

50

[
    1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz',
    'Fizz', 22, 23, 'Fizz', 'Buzz', 26, 'Fizz', 28, 29, 'FizzBuzz', 31, 32, 'Fizz', 34, 'Buzz', 'Fizz', 37, 38, 'Fizz',
    'Buzz', 41, 'Fizz', 43, 44, 'FizzBuzz', 46, 47, 'Fizz', 49, 'Buzz'
]

"""

from itertools import count, cycle, islice


def main():
    n = 50

    fizz_cycle = cycle(["", "", "Fizz"])            # would get a Fizz for multiples of 3
    buzz_cycle = cycle(["", "", "", "", "Buzz"])    # would get a Buzz for multiples of 5

    # would additionally get FizzBuzz for multiples of 15 (Fizz would meet Buzz when the counter is a multiple of 15)
    fizz_buzz_gen = (f + b for f, b in zip(fizz_cycle, buzz_cycle))

    gen = (w or i for w, i in zip(fizz_buzz_gen, count(1)))
    print(list(islice(gen, n)))


if __name__ == "__main__":
    main()
