"""

You have two integer arrays sorted in ascending order and an integer k. Write a Python program to find the k smallest
pairs (u, v) which consist of one element from the first array and one element from the second array using the heap
queue algorithm.

lst1 = [1, 3, 7]
lst2 = [2, 4, 6]
k = 2

->  [(1, 2), (1, 4)]

"""

from heapq import nsmallest
from itertools import product


def main():
    lst1 = [1, 3, 7]
    lst2 = [2, 4, 6]
    k = 2

    print(nsmallest(k, product(lst1, lst2)))


if __name__ == "__main__":
    main()
