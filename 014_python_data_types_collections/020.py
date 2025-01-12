"""

Write a Python program to find the item with the highest frequency in a given list.

[2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2]

(2, 5)

"""

from collections import Counter


def main():
    c = Counter([2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2])
    print(c.most_common(1)[0])


if __name__ == "__main__":
    main()
