"""

Write a Python program that iterates over elements as many times as its count.

Element p is repeated 4 times
Element q is repeated 2 times
Element r is repeated 0 times   (should be ignored)
Element s is repeated -2 times  (should be ignored)

['p', 'p', 'p', 'p', 'q', 'q']

"""

from collections import Counter


def main():
    c = Counter(p=4, q=2, r=0, s=-2)
    print(list(c.elements()))


if __name__ == "__main__":
    main()
