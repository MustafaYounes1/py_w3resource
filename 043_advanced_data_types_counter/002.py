"""

Write a Python program that creates a 'Counter' from a list of elements and print the most common elements along
with their counts.

[1, 2, 3, 4, 5, 11, 3, 3, 6, 7, 8, 9, 3, 10, 1]

-> [(3, 4), (1, 2), (2, 1), (4, 1), (5, 1), (11, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1)]

"""

from collections import Counter


def main():
    lst = [1, 2, 3, 4, 5, 11, 3, 3, 6, 7, 8, 9, 3, 10, 1]
    c = Counter(lst)
    print(c.most_common())


if __name__ == "__main__":
    main()
