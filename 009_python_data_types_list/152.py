"""

Write a Python program to combine two sorted lists using the heapq module.

[1, 3, 5, 7, 9, 11]
[0, 2, 4, 6, 8, 10]

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

"""

import heapq


def main():
    lst1 = [1, 3, 5, 7, 9, 11]
    lst2 = [0, 2, 4, 6, 8, 10]

    print(list(heapq.merge(lst1, lst2)))


if __name__ == "__main__":
    main()
