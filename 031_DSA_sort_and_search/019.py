"""

Write a Python program to sort unsorted numbers using Binary Insertion Sort.

Binary insertion sort is a sorting algorithm which is similar to the insertion sort, but instead of using linear search
to find the location where an element should be inserted, we use binary search. Thus, we reduce the comparative value
of inserting a single element from O(n) to O(log n).

It is a flexible algorithm, which means it works faster when the same given members are already heavily sorted, i.e.,
the current location of the feature is closer to its actual location in the sorted list.

It is a stable sorting algorithm – elements with the same values appear in the same sequence in the last order as they
were in the first list.

========
Approach
========

* Iterate the array from the second element to the last element.
* Store the current element "A[i]" in a variable "key".
* Find the position of the element just greater than "A[i]" in the subarray from "A[0]" to "A[i-1]" using binary search.
  Say this element is at index "pos".
* Shift all the elements from index "pos" to "i-1" towards the right.
* "A[pos] = key"

A good explanation can be found in this YouTube Tutorial: https://www.youtube.com/watch?v=-OVB5pOZJug

Worst / Average Time Complexity:    O(n^2)
Best Time Complexity:               O(n * log(n)) (the num of comparisons for inserting one element is O(log n),
                                    and for N elements, it will be O(n log n).)

[14, 46, 43, 27, 57, 41, 45, 21, 70]

Ascending order:    [14, 21, 27, 41, 43, 45, 46, 57, 70]
Descending order:   [70, 57, 46, 45, 43, 41, 27, 21, 14]

"""


def binary_search(lst: list[...], s: int, e: int, item: ..., reverse: bool) -> int:
    """Find the index of the first element (in the sorted part) that is larger_asc/smaller_desc than the provided item
    using binary search
    Note: the search is limited in the range [s, e] which typically indicates the sorted part of the list"""
    while s <= e:
        mid = s + (e - s) // 2

        # if the middle item is equal to the item to be placed => the target index should be on its right in order to
        # make the algorithm stable
        if item == lst[mid]:
            return mid + 1

        # Ascending Sorting #
        # The sorted part would be sorted in ascending order
        # we need to find the index of the first element that is larger than the item to be placed
        # => if lst[mid] > item => search in the left half
        # => if lst[mid] < item => search in the right half

        # Descending Sorting #
        # The sorted part would be sorted in descending order
        # we need to find the index of the first element that is smaller than the item to be placed
        # => if lst[mid] > item => search in the right half
        # => if lst[mid] < item => search in the left half

        elif [item > lst[mid], item < lst[mid]][reverse]:
            s = mid + 1

        else:
            e = mid - 1

    # once the three pointers: s, e, and m are pointing to the same pointer => the loop would execute only one further
    # pass, and the pointer s after executing the final pass would be pointing to the target position

    return s


def binary_insertion_sort(lst: list[...], reverse: bool = False) -> None:
    """Binary Insertion Sort Implementation"""
    for idx, item in enumerate(lst[1:], start=1):
        j = idx - 1  # the upper bound of the sorted part

        # Find the correct place in the sorted part of the array to insert the current item using binary search
        # We would like to insert the current item at the location of the first element (in the sorted part) that is
        # larger_asc/smaller_desc than the item to be inserted.
        target_idx = binary_search(lst, 0, j, item, reverse)

        # before placing the item at the target location, items in the range [target_location, j] needs to be
        # shifted to the right
        while j >= target_idx:
            lst[j + 1] = lst[j]
            j -= 1

        # place the current item at its target location
        lst[target_idx] = item


def main():
    lst = [14, 46, 43, 27, 57, 41, 45, 21, 70]
    lst1 = lst[:]  # shallow copy

    binary_insertion_sort(lst, False)
    print(lst)

    binary_insertion_sort(lst1, True)
    print(lst1)


if __name__ == "__main__":
    main()
