"""

Write a Python program to generate permutations of n items.

n = 3   =>  [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]

"""

from itertools import permutations


def main():
    print(list(permutations(range(3))))


if __name__ == "__main__":
    main()
