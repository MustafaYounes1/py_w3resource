"""

Write a Python program to print all permutations with a given repetition number of characters of a given string.

'xyz', 2
[('x', 'x'), ('x', 'y'), ('x', 'z'), ('y', 'x'), ('y', 'y'), ('y', 'z'), ('z', 'x'), ('z', 'y'), ('z', 'z')]

"""

from itertools import product


def main():
    s = 'xyz'
    print(list(product(s, repeat=2)))


if __name__ == "__main__":
    main()
