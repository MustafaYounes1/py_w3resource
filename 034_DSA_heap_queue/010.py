"""

Given a n x n matrix where each of the rows and columns is sorted in ascending order, write a Python program to find
the kth smallest element in the matrix using the heap queue algorithm.

matrix = [
   [0, 5, 9],
   [11, 12, 13],
   [15, 17, 19]
]

Third-smallest element:     9

"""

from heapq import merge, nsmallest


def main():
    matrix = [
        [0, 5, 9],
        [11, 12, 13],
        [15, 17, 19]
    ]
    k = 3

    sorted_merge = list(merge(*matrix))
    assert 1 <= k <= len(sorted_merge)
    print(sorted_merge[k-1])


if __name__ == "__main__":
    main()
