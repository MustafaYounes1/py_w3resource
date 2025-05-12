"""

Write a Python program to sort a list of elements using the merge sort algorithm.

The Merge Sort algorithm is a divide-and-conquer algorithm that sorts an array by first breaking it down into smaller
arrays, and then building the array back together the correct way so that it is sorted.

Divide: The algorithm starts with breaking up the array into smaller and smaller pieces until one such sub-array only
        consists of one element.

Conquer: The algorithm merges the small pieces of the array back together by putting the lowest values first,
        resulting in a sorted array.

How it works
    1.  Divide the unsorted array into two sub-arrays, half the size of the original.
    2.  Continue to divide the sub-arrays as long as the current piece of the array has more than one element.
    3.  Merge two sub-arrays together by always putting the lowest value first.
    4.  Keep merging until there are no sub-arrays left.

Time Complexity
    Best	O(n * log n)
    Average	O(n * log n)
    Worst	O(n * log n)

Space complexity: O(n)

[14, 46, 43, 27, 57, 41, 45, 21, 70]

Ascending order:    [14, 21, 27, 41, 43, 45, 46, 57, 70]
Descending order:   [70, 57, 46, 45, 43, 41, 27, 21, 14]

"""


def merge_sort_out_of_place(lst: list[...], reverse: bool = False) -> list[...]:
    """Implement recursive out-of-place merge sort on an input list"""

    def merge(ls: list[...], rs: list[...]) -> list[...]:
        """Implement the merge routine - merge two sorted halves"""
        res = []
        i = j = 0

        # At the end of this loop one side (or both sides) would be completely consumed
        while i < len(ls) and j < len(rs):
            if [ls[i] < rs[j], ls[i] > rs[j]][reverse]:
                res.append(ls[i])
                i += 1
            else:
                res.append(rs[j])
                j += 1

        # Get the leftovers from left/right side if there are any
        res.extend(ls[i:])
        res.extend(rs[j:])

        return res

    if len(lst) <= 1:
        return lst

    # splitting step
    mid = len(lst) // 2

    # apply merge sort on the left side (returns a sorted left side)
    left_side = merge_sort_out_of_place(lst[:mid], reverse)

    # apply merge sort on the right side (returns a sorted right side)
    right_side = merge_sort_out_of_place(lst[mid:], reverse)

    # merging step
    return merge(left_side, right_side)


def merge_sort(lst: list[...], reverse: bool = False) -> None:
    """Implement recursive in-place merge sort on an input list"""

    # break the recursion when the input list has only one item + do nothing if the input list has one or zero items
    if len(lst) <= 1:
        return

    # Splitting step - split the input list into two halves
    mid = len(lst) // 2
    left_side = lst[:mid]
    right_side = lst[mid:]

    # Apply recursion on each side to finally get sorted left/right sides of one element
    merge_sort(left_side, reverse)  # apply in-place merge sort on the left side (returns a sorted left side)
    merge_sort(right_side, reverse)  # apply in-place merge sort on the right side (returns a sorted right side)

    # Merging step
    # the input list at each iteration would be sorted based on its already sorted left and right sides
    # at the deepest level, left and right sides would have only one item and are already sorted
    # this would back up sorted left/right sides to the uplevel call, and recursively the input list would have
    # two sides that are already sorted and the sorted sides would be used to sort the current input list in-place
    i = j = k = 0

    # At the end of this loop one side (or both sides) would be completely consumed
    while i < len(left_side) and j < len(right_side):
        if [left_side[i] < right_side[j], left_side[i] > right_side[j]][reverse]:
            lst[k] = left_side[i]
            i += 1
        else:
            lst[k] = right_side[j]
            j += 1
        k += 1

    # Get the leftovers from the left side if there are any
    while i < len(left_side):
        lst[k] = left_side[i]
        i += 1
        k += 1

    # Get the leftovers from the right side if there are any
    while j < len(right_side):
        lst[k] = right_side[j]
        j += 1
        k += 1



def main():
    lst = [14, 46, 43, 27, 57, 41, 45, 21, 70]
    lst1 = lst[:]  # shallow copy

    merge_sort(lst, False)
    print(lst)

    merge_sort(lst1, True)
    print(lst1)


if __name__ == "__main__":
    main()
