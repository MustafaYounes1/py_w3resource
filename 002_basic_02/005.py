"""

Write a Python program to make combinations of 3 digits.

"""

from itertools import permutations


def main():
    digits = [str(_) for _ in [1, 2, 3]]
    for comb in permutations(digits, 3):
        print("".join(comb))


if __name__ == "__main__":
    main()
