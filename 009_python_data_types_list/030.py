"""

Write a Python program to get the frequency of elements in a list.

[10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]
{10: 4, 20: 4, 40: 2, 50: 2, 30: 1}

"""

from collections import Counter


def main():
    lst = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]
    print(dict(Counter(lst)))


if __name__ == "__main__":
    main()
