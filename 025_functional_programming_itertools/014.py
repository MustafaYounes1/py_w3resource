"""

Write a Python program to generate all possible permutations of n different objects.

[1]         =>  [(1,)]
[1, 2]      =>  [(1, 2), (2, 1)]
[1, 2, 3]   =>  [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

"""

from itertools import permutations


def main():
    data = [
        [1],
        [1, 2],
        [1, 2, 3]
    ]

    for _ in data:
        print(list(permutations(_)))


if __name__ == "__main__":
    main()
