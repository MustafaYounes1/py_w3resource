"""

Write a Python program to find repeated items in a tuple.

2, 4, 5, 6, 2, 3, 4, 4, 7

[2, 4]

"""

from collections import Counter


def main():
    t = 2, 4, 5, 6, 2, 3, 4, 4, 7
    c = Counter(t)
    print([_ for _ in c if c[_] > 1])


if __name__ == "__main__":
    main()
