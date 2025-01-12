"""

Write a Python program to find the left difference between two lists including duplicate elements.
Note: use the collection module

lst1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
lst2 = [1, 1, 2, 4, 5, 6]

[3, 3, 4, 7]

"""

from collections import Counter


def main():
    lst1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
    lst2 = [1, 1, 2, 4, 5, 6]

    print(list((Counter(lst1) - Counter(lst2)).elements()))


if __name__ == "__main__":
    main()
