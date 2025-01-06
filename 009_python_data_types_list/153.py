"""

Write a Python program to check if a given element occurs at least n times in a list.

[0, 1, 3, 5, 0, 3, 4, 5, 0, 8, 0, 3, 6, 0, 3, 1, 1, 0]

Check if 3 occurs at least 4 times =>   True
Check if 0 occurs at least 5 times =>   True
Check if 8 occurs at least 3 times =>   False

"""

from collections import Counter


def main():
    lst = [0, 1, 3, 5, 0, 3, 4, 5, 0, 8, 0, 3, 6, 0, 3, 1, 1, 0]
    data = [
        [3, 4],
        [0, 5],
        [8, 3]
    ]

    c = dict(Counter(lst))
    for el, f in data:
        print(c[el] >= f)


if __name__ == "__main__":
    main()
