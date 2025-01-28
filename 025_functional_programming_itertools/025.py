"""

Write a Python program to find the nth Hamming number. Use the itertools module.

Hamming numbers are numbers of the form:    H = 2^i x 3^j x 5^k Where i, j, k ≥ 0
The sequence of Hamming numbers 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27. . .

8   =>  9
14  =>  20
17  =>  27

"""

from itertools import islice
from typing import Generator


def ham_gen() -> Generator[int, None, None]:
    bases = [2, 3, 5]
    expos = [0, 0, 0]
    hams = [1]

    yield hams[-1]

    # infinite generator
    while True:
        next_hams = [bases[i] * hams[expos[i]] for i in range(3)]
        next_ham = min(next_hams)
        hams.append(next_ham)

        yield hams[-1]

        for i in range(3):
            expos[i] += int(next_hams[i] == next_ham)


def nth_ham(n: int) -> int:
    return list(islice(ham_gen(), n))[-1]


def main():
    print(nth_ham(8))
    print(nth_ham(14))
    print(nth_ham(17))


if __name__ == "__main__":
    main()
