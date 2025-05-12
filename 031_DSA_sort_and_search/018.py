"""

Write a Python program to sort a list of elements using Radix sort.

According to Wikipedia "In computer science, radix sort is a non-comparative integer sorting algorithm that sorts data
with integer keys by grouping keys by the individual digits which share the same significant position and value".

Radix Sort is a linear sorting algorithm that sorts elements by processing them digit by digit. It is an efficient
sorting algorithm for integers or strings with fixed-size keys.

The key idea behind Radix Sort is to exploit the concept of "place value". It assumes that sorting numbers digit by
digit will eventually result in a fully sorted list.

Radix Sort can be performed using different variations, such as Least Significant Digit (LSD) Radix Sort or Most
Significant Digit (MSD) Radix Sort.

The radix (or base) is the number of unique digits in a number system. In the decimal system we normally use, there
are 10 different digits from 0 till 9. Radix Sort uses the radix so that decimal values are put into 10 different
buckets (or containers) corresponding to the digit that is in focus, then put back into the array before moving on to
the next digit.

==============
Stable Sorting
==============
A stable sorting algorithm is an algorithm that keeps the order of elements with the same value before and after the
sorting. Let's say we have two elements "K" and "L", where "K" comes before "L", and they both have value "3".
A sorting algorithm is considered stable if element "K" still comes before "L" after the array is sorted.

Radix Sort must sort the elements in a stable way for the result to be sorted correctly.

After sorting the elements on the least significant digit and moving to the next digit, it is important to not destroy
the sorting work that has already been done on the previous digit position, and that is why we need to take care that
Radix Sort does the sorting on each digit position in a stable way.

=========
Approach
=========
1. Find the largest element in the array , i.e. "max". Let "X" be the number of digits in "max".
    "X" is calculated because we have to go through all the significant places of all elements.

2. Now, go through each significant place one by one.
    * Use any stable sorting technique to sort the digits at each significant place (e.g., Count Sort)

    * Start with the least significant digit (rightmost digit) (unit place digits)

    * Sort the values based on the digit in focus by first putting the values in the correct bucket based on the digit
    in focus, and then put them back into array in the correct order.

    * Move to the next digit (digits at unit place -> digits at tens place -> digits at hundreds place -> ...),
    and sort again, like in the step above, until there are no digits left.

A good explanation can be found in this YouTube Tutorial: https://www.youtube.com/watch?v=XiuSW_mEn7g

Time Complexity:    O(d * (n + b)),
                    where d is the number of digits,
                    n is the number of elements,
                    and b is the base of the number system being used.

Space Complexity:   O(n + b)
                    This space complexity comes from the need to create buckets for each digit value and to copy the
                    elements back to the original array after each digit has been sorted.

Note: radix sort has linear time complexity which is better than O(n * log n) of comparative sorting algorithms.
If we take very large digit numbers or the number of other bases like 32-bit and 64-bit numbers then it can perform
in linear time however the intermediate sort takes large space.

[14, 46, 43, 27, 57, 41, 45, 21, 70]

Ascending order:    [14, 21, 27, 41, 43, 45, 46, 57, 70]
Descending order:   [70, 57, 46, 45, 43, 41, 27, 21, 14]

"""

from itertools import accumulate


def count_sort(lst: list[int], place: int, reverse: bool, base: int = 10) -> None:
    """An implementation of Count Sort on non-negative integers while focusing on the provided significant place/digit.
    Note: It's required for the Radix Sort to use an intermediate stable sorting algorithm, that's why Count Sort was
    used, however, any other stable algorithm could be used instead for sorting while focusing on the provided
    significant place/digit"""

    # Initialize the count list - map [0, 9] (when base = 10) to counts
    count = [0] * base

    # Initialize the auxiliary array
    aux = [0] * len(lst)

    # counting - the significant digits of the input array's items would be indices in the count array
    for _ in lst:
        d = (_ // place) % base  # get the significant place of the current item
        count[d] += 1

    # Get the cumulative sum of the counts - would help to calculate the index of items of the input list in the
    # auxiliary space
    if not reverse:
        count = list(accumulate(count))
    else:
        # the counts for descending order should be accumulated from right to left
        for i in range(len(count) - 2, -1, -1):
            count[i] += count[i + 1]

    # loop through the input list in reverse order to preserve the order of the identical items (stable algorithm)
    # calculate the corresponding positions of the input list's items in the output list
    for i in range(len(lst) - 1, -1, -1):
        d = (lst[i] // place) % base
        aux[count[d] - 1] = lst[i]
        count[d] -= 1

    # Copy the values from the auxiliary space to the input list
    for i, _ in enumerate(aux):
        lst[i] = _


def non_negative_ints(lst: list[int]) -> bool:
    """Check whether all entries in a list are positive integers"""
    return all(isinstance(_, int) and _ >= 0 for _ in lst)


def radix_sort(lst: list[int], reverse: bool = False) -> None:
    """An in-place implementation of the Least Significant Digit (LSD) Radix Sort that works on integers with b=10"""
    if not lst:
        return

    if not non_negative_ints(lst):
        raise ValueError("This implementation of Radix Sort works only on non-negative integers")

    ma = max(lst)  # maximum element from which the required number of places would be inferred
    place = 1  # start with the digits at the unit place

    # Radix Sort on all significant places
    while ma // place > 0:
        count_sort(lst, place, reverse)  # Apply Count Sort on the current significant place
        place *= 10  # shift the current significant place/digit to the left (tens -> hundreds -> thousands -> ... )


def main():
    lst = [14, 46, 43, 27, 57, 41, 45, 21, 70]
    lst1 = lst[:]  # shallow copy

    radix_sort(lst, False)
    print(lst)

    radix_sort(lst1, True)
    print(lst1)


if __name__ == "__main__":
    main()
