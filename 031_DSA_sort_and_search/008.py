"""

Write a Python program to sort a list of elements using the quick sort algorithm.

QuickSort is a sorting algorithm works on the principle of Divide and Conquer breaking down the problem into smaller
sub-problems. It picks an element as a pivot and partitions the given array around the picked pivot by placing the
pivot in its correct position in the sorted array.

While dividing/partitioning the array, the pivot element should be positioned in such a way that elements less than
pivot are kept on the left side and elements greater than pivot are on the right side of the pivot.

There are mainly three steps in the algorithm:

1. Choose a Pivot:      Select an element from the array as the pivot. The choice of pivot can vary (e.g., first element,
                        last element, random element, or median).

2. Partition the Array: Rearrange the array around the pivot. After partitioning, all elements smaller than the pivot
                        will be on its left, and all elements greater than the pivot will be on its right. The pivot
                        is then in its correct position, and we obtain the index of the pivot.

3. Recursively Call:    Recursively apply the same process to the two partitioned sub-arrays (left and right of the pivot).

4. Base Case:           The recursion stops when there is only one element left in the sub-array, as a single element
                        is already sorted.

Time Complexity
    Best	O(n * log n)
        Occurs when the pivot element divides the array into two equal halves.
        i.e. the pivot element is always the middle element in the sub array or near to the middle element.
    Average	O(n * log n)
    Worst	O(n^2)
        It occurs when the pivot element picked is either the greatest or the smallest element.
        This condition leads to the case in which the pivot element lies in an extreme end of the sorted array.
        One sub-array is always empty and another sub-array contains n - 1 elements. Thus, quicksort is called only
        on this sub-array.

Space Complexity: O(n)

[14, 46, 43, 27, 57, 41, 45, 21, 70]

Ascending order:    [14, 21, 27, 41, 43, 45, 46, 57, 70]
Descending order:   [70, 57, 46, 45, 43, 41, 27, 21, 14]

"""

import random


def quick_sort_simple_out_of_place(lst: list[...], reverse: bool = False) -> list[...]:
    """A simple recursive out-of-place implementation of Quick Sort with the pivot as the last element"""
    if len(lst) <= 1:
        return lst

    pivot = lst[-1]
    left, right = [], []

    for _ in lst[:-1]:
        if [_ < pivot, _ >= pivot][reverse]:
            left.append(_)
        else:
            right.append(_)


    return quick_sort_simple_out_of_place(left, reverse) + [pivot] + quick_sort_simple_out_of_place(right, reverse)


def partition(lst: list[...], s: int, e: int, reverse: bool) -> int:
    """Partition an input list having the pivot in its correct position with all smaller elements on its left and
    greater elements on its right (The pivot is considered as the last element) and return the index of the selected
    pivot after being positioned in its correct location"""
    pivot = lst[e]  # choose the pivot as the last element in the input list

    i = s - 1  # a pointer that would point to the last element that is smaller than the pivot

    for j in range(s, e):
        if [lst[j] < pivot, lst[j] > pivot][reverse]:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]  # In case an item that is greater than the pivot was found earlier, i+1
            # should point to it, and it should be swapped with the current item (smaller that the pivot) that was
            # found to have smaller items on the pivot left and greater items on its right.

    # At the end, swap the pivot with the smallest element that is greater than the pivot. This would modify the list
    # in such a way where elements smaller than the pivot are on its left and elements larger than the pivot are on its
    # right
    lst[e], lst[i+1] = lst[i+1], lst[e]

    # return the new pivot position to divide and conquer the input list around that position
    return i + 1


def quick_sort(lst: list[...], reverse: bool = False, random_pivot: bool = False) -> None:
    """A recursive in-place implementation of Quick Sort with the pivot as either the last element or a random element
    Note: When random_pivot is set to False the chosen pivot would simply be the last element
          To further improve the time complexity of the algorithm, random_pivot shall be set to True and the
            algorithm would simply choose a random element and swap it with the last element in order to reuse the
            existing 'pivot as the last element' logic."""

    def helper(ll: list[...], s: int, e: int) -> None:
        if e > s:
            # if random pivot is chosen
            if random_pivot:
                rand_idx = random.choice(range(s, e + 1))  # find a random element in the input indices range
                lst[e], lst[rand_idx] = lst[rand_idx], lst[e]  # swap with the last element to reuse the existing logic

            pivot_idx = partition(ll, s, e, reverse)
            helper(ll, s, pivot_idx - 1)
            helper(ll, pivot_idx + 1, e)

    helper(lst, 0, len(lst) - 1)


def main():
    lst = [14, 46, 43, 27, 57, 41, 45, 21, 70]
    lst1 = lst[:]  # shallow copy

    quick_sort(lst, False, False)
    print(lst)

    quick_sort(lst1, True, False)
    print(lst1)


if __name__ == "__main__":
    main()
