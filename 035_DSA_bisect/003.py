"""

Write a Python program to implement insertion sort using bisect module.

[25, 45, 36, -47, 69, 48, 68, -78, 14, -36]

Ascending order:    [-78, -47, -36, 14, 25, 36, 45, 48, 68, 69]
Descending order:   [69, 68, 48, 45, 36, 25, 14, -36, -47, -78]

"""

from bisect import bisect, insort


def naive_insertion_sort(lst: list[int], reverse: bool = True) -> list[int]:
    """Naive out-of-place implementation"""
    res = []

    if not lst:
        return res

    res = [lst[0]]
    for item in lst[1:]:
        insort(res, item, key=lambda el: -el if reverse else el)

    return res


def insertion_sort(lst: list[int], reverse: bool = False) -> None:
    """An in-place implementation"""
    if not lst:
        return

    for i, item in enumerate(lst[1:], start=1):
        # bisect should get '-item' if the sorting is in the descending order
        # From the doc: 'To support searching complex records, the key function is not applied to the x value.'
        # whereas insort in the out-of-place implementation above should take 'item'
        # From the doc: 'To support inserting records in a table, the key function (if any) is applied to x for the
        # search step but not for the insertion step.'
        target_idx = bisect(lst, -item if reverse else item, lo=0, hi=i, key=lambda el: -el if reverse else el)
        j = i - 1

        # shift elements to the right and places the current item at target_idx, modifying the list in place.
        while j >= target_idx:
            lst[j + 1] = lst[j]
            j -= 1

        lst[target_idx] = item


def main():
    lst = [25, 45, 36, -47, 69, 48, 68, -78, 14, -36]
    lst1 = lst[:]  # shallow copy

    # print(naive_insertion_sort(lst, False))
    # print(naive_insertion_sort(lst, True))

    insertion_sort(lst, False)
    print(lst)

    insertion_sort(lst1, True)
    print(lst1)


if __name__ == "__main__":
    main()
