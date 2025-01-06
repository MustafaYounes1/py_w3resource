"""

Write a Python program that creates all possible strings using the letters 'a', 'e', 'i', 'o', and 'I'.
Ensure that each character is used only once.

"""

from itertools import permutations


def main():
    chars = "aeioI"
    for seq in permutations(chars, 5):
        print("".join(seq))


if __name__ == "__main__":
    main()
