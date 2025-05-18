"""

Write a Python function that accepts an arbitrary list and converts it to a heap using the heap queue algorithm.

[25, 44, 68, 21, 39, 23, 89]    =>  [21, 25, 23, 44, 39, 68, 89]

"""

from heapq import heapify


def main():
    lst = [25, 44, 68, 21, 39, 23, 89]

    heapify(lst)
    print(lst)


if __name__ == "__main__":
    main()
