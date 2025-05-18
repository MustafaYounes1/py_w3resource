"""

Write a Python program to implement heapsort by pushing all values onto a heap and then popping off the smallest
values one at a time.

[1, 3, 5, 7, 9, 2, 4, 6, 8, 0]

Ascending order:        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Descending order:       [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

"""

from heapq import heappush, heappop


def heap_sort(lst: list[...], reverse: bool = False) -> list[...]:
    """Heap sort implementation"""
    m_heap, res = [], []

    # push element into the min heap one by one while maintaining the heap property
    for _ in lst:
        heappush(m_heap, _)

    # get the sorted values from the min heap via popping without breaking the heap property
    for _ in range(len(lst)):

        # ascending order
        if not reverse:
            res.append(heappop(m_heap))

        # descending order
        else:
            res = [heappop(m_heap)] + res

    return res


def main():
    lst = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]

    print(heap_sort(lst, False))
    print(heap_sort(lst, True))


if __name__ == "__main__":
    main()
