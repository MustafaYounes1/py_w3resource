"""

Write a Python program to compute the sum of digits of each number in a given list of positive integers.

[10, 2, 56]         =>  14
[10, 20, 4, 5, 70]  =>  19

"""

from itertools import chain


def main():
    data = [
        [10, 2, 56],
        [10, 20, 4, 5, 70]
    ]

    for _ in data:
        print(sum(int(__) for __ in chain.from_iterable(map(str, _))))


if __name__ == "__main__":
    main()
