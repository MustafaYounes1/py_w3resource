"""

Write a Python program to compute the maximum product of three numbers in a given array of n integers using the heap
queue algorithm.

[12, 74, 9, 50, 61, 41]     =>  225700
[-10, -3, 5, 6, -20]        =>  1200

"""

from heapq import nlargest, nsmallest
import math


def max_triplet_product(lst: list[int | float]) -> int | float:
    """Return the max triplet product in a given list"""
    assert len(lst) > 3, "invalid input"

    # In triplets, there will either be 2 negative elements and 1 positive element or all 3 positive elements so that
    # resultant product will be positive.
    largest_3, smallest_two = nlargest(3, lst), nsmallest(2, lst)

    return max(math.prod(largest_3), math.prod([largest_3[0]] + smallest_two))


def main():
    data = [
        [12, 74, 9, 50, 61, 41],
        [-10, -3, 5, 6, -20]
    ]

    for _ in data:
        print(max_triplet_product(_))


if __name__ == "__main__":
    main()
