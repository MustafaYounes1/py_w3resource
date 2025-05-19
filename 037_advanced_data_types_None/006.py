"""

Write a Python program that defines a dictionary and retrieves a value using a key. If the key is not found, return None.

"""

from collections import defaultdict


def main():
    d: defaultdict[int, int | None] = defaultdict(lambda: None)
    d[1] = 1
    print(d[1], d[0])


if __name__ == "__main__":
    main()
