"""

Write a Python program to find the kth (1 <= k <= array's length) largest element in an unsorted array using the heap
queue algorithm.

[12, 14, 9, 50, 61, 41]

Third-largest element:  41
Second-largest element: 50
Fifth-largest element:  12

"""

from heapq import heapify, nlargest


def kth_largest(lst: list[...], k: int) -> ...:
    """Get the kth largest element from an unsorted list"""
    assert lst and 1 <= k <= len(lst), "invalid inputs"

    # heapify is in-place function -> get a shallow copy in order not to directly heapify the source list
    ll = lst[:]
    heapify(ll)

    return nlargest(k, ll)[k - 1]


def main():
    lst = [12, 14, 9, 50, 61, 41]

    print(kth_largest(lst, 3))
    print(lst)
    print(kth_largest(lst, 2))
    print(kth_largest(lst, 5))


if __name__ == "__main__":
    main()
