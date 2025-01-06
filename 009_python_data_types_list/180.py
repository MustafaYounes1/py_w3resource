"""

Write a Python program to create the smallest possible number using the elements of a given list of positive integers.

[3, 40, 41, 43, 74, 9]      =>  3404143749
[10, 40, 20, 30, 50, 60]    =>  102030405060
[8, 4, 2, 9, 5, 6, 1, 0]    =>  01245689

"""

from itertools import permutations


def main():
    data = [
        [3, 40, 41, 43, 74, 9],
        [10, 40, 20, 30, 50, 60],
        [8, 4, 2, 9, 5, 6, 1, 0]
    ]

    for _ in data:
        tmp = list("".join(__) for __ in permutations(map(str, _)))
        print(min(tmp, key=int))


if __name__ == "__main__":
    main()
