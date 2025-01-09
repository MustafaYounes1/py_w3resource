"""

Write a Python program to find the specified number of maximum values in a given dictionary.

{'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}

1   =>  ['f']
2   =>  ['f', 'i']
5   =>  ['f', 'i', 'g', 'd', 'c']

"""

from heapq import nlargest


def main():
    d = {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
    for n in (1, 2, 5):
        print(nlargest(n, d, d.get))


if __name__ == "__main__":
    main()
