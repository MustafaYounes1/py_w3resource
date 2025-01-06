"""

Write a Python program to find the list of words that are longer than n from a given list of words.

The quick brown fox jumps over the lazy dog, 3

['quick', 'brown', 'jumps', 'over', 'lazy']

"""


def main():
    lst = "The quick brown fox jumps over the lazy dog".split()
    n = 3
    print(list(filter(lambda _: len(_) > n, lst)))


if __name__ == "__main__":
    main()
