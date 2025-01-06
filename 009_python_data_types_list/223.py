"""

Write a Python program to create a list with non-unique values filtered out.

[1, 2, 2, 3, 4, 4, 5]   =>  [1, 3, 5]

"""

from collections import Counter


def main():
    lst = [1, 2, 2, 3, 4, 4, 5]
    print([_ for _, count in Counter(lst).items() if count == 1])


if __name__ == "__main__":
    main()
