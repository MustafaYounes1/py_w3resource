"""

Write a Python program to sort a list of elements using 3-way Quick Sort.

In simple QuickSort algorithm, we select an element as pivot, partition the array around a pivot and recur for
sub-arrays on the left and right of the pivot.

Normal Quicksort exhibits poor performance for inputs that contain many repeated elements. The problem is clearly
apparent when all the input elements are equal: at each recursion, the left partition is empty (no input values are
less than the pivot), and the right partition has only decreased by one element (the pivot is removed).

To solve this problem, we use 3-way quick sort (that is based on Dutch National Flag algorithm).
Values equal to the pivot are already sorted so only left and right partitions have to be sorted using recursion.

In this algorithm, the original array is partitioned into three parts that are as follows:
    * One with elements less than pivot,
    * Second with equal to pivot and
    * Last with elements greater than pivot.

Best Time Complexity:       O(n * log(n))
Average Time Complexity:    O(n * log(n))
Worst Time Complexity:      O(n^2)

Space Complexity:           O(log(n))

[14, 46, 43, 27, 57, 41, 45, 21, 70]

Ascending order:    [14, 21, 27, 41, 43, 45, 46, 57, 70]
Descending order:   [70, 57, 46, 45, 43, 41, 27, 21, 14]

"""

import random


def partition_3w(lst: list[...], s: int, e: int, reverse: bool) -> tuple[int, int]:
    """Based on the Dutch National Flag algorithm, partition the array around the pivot (the last element) into
    three partitions (less, equal, larger) and return a tuple of two integers:
        * the index of the last element in the 'less' section
        * the index of the first element in the 'larger' section
    """
    pivot = lst[e]  # choose the pivot as the last element in the input list

    i = j = s
    k = e

    # Dutch National Flag algorithm #
    # i would start at 's' and move to the right as we get an element that is less than the pivot
    # k would start at the 'e' and move to the left as we get an element that is larger than the pivot
    # j is the index of the current item
    #   swap it with lst[i] if the current item is less than the pivot
    #   swap it with lst[k] if the current item is greater than the pivot

    # at the end of this function call #
    # lst[s: i]   ->  elements smaller than the pivot
    # lst[i: j]   ->  elements smaller equal to the pivot
    # lst[k+1:]   ->  elements larger than the pivot

    while j <= k:
        if [lst[j] < pivot, lst[j] > pivot][reverse]:
            lst[i], lst[j] = lst[j], lst[i]
            # both i and j should go one step to the right
            i += 1
            j += 1

        elif lst[j] == pivot:
            j += 1  # j should go step to the right

        else:
            lst[j], lst[k] = lst[k], lst[j]
            k -= 1  # k should go one step to the left
            # note that j shouldn't be moved to the right here, it could now get a value that is smaller than
            # the pivot -> so we need to check it again

    return i - 1, k + 1


def quick_sort_3w(lst: list[...], reverse: bool = False, random_pivot: bool = False) -> None:
    """An implementation of the 3-Way Quick Sort algorithm
    Note: when random pivot is set to False, the pivot is considered the last element"""

    def helper(ll: list[...], s: int, e: int) -> None:
        if e > s:
            if random_pivot:
                rand_idx = random.choice(range(s, e + 1))  # find a random element in the input indices range
                lst[e], lst[rand_idx] = lst[rand_idx], lst[e]  # swap with the last element to reuse the existing logic

            lt, gt = partition_3w(lst, s, e, reverse)  # partition into 3 groups (less, equal, larger)
            helper(ll, s, lt)  # call on the left partition tha has elements less than the pivot
            helper(ll, gt, e)  # call on the right partition tha has elements larger than the pivot

    helper(lst, 0, len(lst) - 1)


def main():
    lst = [14, 46, 43, 27, 57, 41, 45, 21, 70]
    lst1 = lst[:]  # shallow copy

    quick_sort_3w(lst, False, False)
    print(lst)

    quick_sort_3w(lst1, True, False)
    print(lst1)


if __name__ == "__main__":
    main()
