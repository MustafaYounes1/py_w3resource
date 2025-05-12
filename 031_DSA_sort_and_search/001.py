"""

Write a Python program that implements binary search.
    Return -1 if the item does not exist, otherwise return its index

In computer science, a binary search or half-interval search algorithm finds the position of a target value within a
sorted array. The binary search algorithm can be classified as a dichotomies divide-and-conquer search algorithm and
executes in logarithmic time.

Time Complexities (#instructions required)
    Best case complexity:       O(1)
    Average case complexity:    O(log n)
    Worst case complexity:      O(log n)

Space Complexity (extra memory required)
    The space complexity of the iterative binary search is O(1) (no extra memory is required, the amount of memory
    required is constant doesn't depend on the data being processed522222222222222222222222222222222222222222)
    The space complexity of the recursive binary search is O(log n) (Recursion creates call stack)

[1], 1                          -> 0
[4, 5], 1                       -> -1
[1, 2, 3, 5, 8], 6              -> -1
[1, 2, 3, 5, 8], 5              -> 3
[10, 11, 15, 60, 70, 90], 90    -> 5
[10, 11, 15, 60, 70, 80], 11    -> 1
[10, 11, 15, 60, 70, 80], 10    -> 0

"""


def binary_search_iterative(lst: list[...], obj: ...) -> int:
    """Binary search iterative approach"""
    s, e = 0, len(lst) - 1

    while s <= e:
        mid = s + (e - s) // 2

        if lst[mid] == obj:
            return mid

        elif lst[mid] > obj:
            e = mid - 1

        else:
            s = mid + 1

    return -1


def binary_search_recursive(lst: list[...], obj: ...) -> int:
    """Binary search recursive approach"""

    def helper(s: int, e: int) -> int:
        if s > e:
            return -1

        mid = s + (e - s) // 2

        if lst[mid] == obj:
            return mid

        elif lst[mid] > obj:
            return helper(s, mid - 1)

        else:
            return helper(mid + 1, e)

    return helper(0, len(lst) - 1)


def main():
    data = [
        ([1], 1),
        ([4, 5], 1),
        ([1, 2, 3, 5, 8], 6),
        ([1, 2, 3, 5, 8], 5),
        ([10, 11, 15, 60, 70, 90], 90),
        ([10, 11, 15, 60, 70, 80], 11),
        ([10, 11, 15, 60, 70, 80], 10)
    ]

    for lst, item in data:
        print(binary_search_recursive(lst, item))


if __name__ == "__main__":
    main()
