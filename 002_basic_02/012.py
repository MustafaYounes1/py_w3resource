"""

Write a Python program that generates a list of all possible permutations from a given collection of distinct numbers.

"""

from itertools import permutations


def main():
    seq = input("Enter a list of space-separated integers: ").split()
    for p in permutations(seq, len(seq)):
        print("".join(p))


if __name__ == "__main__":
    main()
