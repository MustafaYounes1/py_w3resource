"""

Write a Python program for counting sort.

Counting Sort is a non-comparison-based sorting algorithm. It is particularly efficient when the range of input values
is small compared to the number of elements to be sorted. The basic idea behind Counting Sort is to count the frequency
of each distinct element in the input array and use that information to place the elements in their correct sorted
positions.

In other words it sorts a collection of objects according to keys that are small integers; that is, it is an integer
sorting algorithm. It operates by counting the number of objects that have each distinct key value, and using
arithmetic on those counts to determine the positions of each key value in the output sequence.

1. Initialize an auxiliary array of length max+1 with all elements as 0s.
2. Go through the array that needs to be sorted and store the count of each element at their respective index in
    count array.
3. Store cumulative sum of the elements of the count array. It helps in placing the elements into the correct index of
    the sorted array. count[i] now contains actual position of the item in output array
3. Iterate from end of the input array and because traversing input array from end preserves the order of equal
    elements, which eventually makes this sorting algorithm stable.
4. Find the index of each element of the original array in the sorted array using the following math:
     outputArray[ countArray[ inputArray[i] ] – 1] = inputArray[i]
     After placing each element at its correct position, decrease its count by one in the count array.

=========================
Limitations of Count Sort
=========================
* Integer values: Counting Sort relies on counting occurrences of distinct values, so they must be integers.
With integers, each value fits with an index (for non negative values), and there is a limited number of different
values, so that the number of possible different values k is not too big compared to the number of values n

* No-negative values: Counting Sort is usually implemented by creating an array for counting. When the algorithm goes
through the values to be sorted, value x is counted by increasing the counting array value at index x. If we tried
sorting negative values, we might get in trouble with sorting value -3, because index -3 might be outside the counting
array or even coincide with the index of a positive element if it was implemented in the original way.

* Limited range of values: If the number of possible different values to be sorted k is larger than the number of
values to be sorted n, the counting array we need for sorting will be larger than the original array we have that
needs sorting, and the algorithm becomes ineffective.

Its running time is linear in the number of items and the difference between the maximum and minimum
key values, so it is only suitable for direct use in situations where the variation in keys is not significantly
greater than the number of items. However, it is often used as a subroutine in another sorting algorithm,
radix sort, that can handle larger keys more efficiently

Best/Average/Worst Time Complexity
    can be expressed in identical forms: O(n + k) or O(n + max) or O(n + m)
    where
        n is the size of the original array
        k is the range of possible values
        max is the maximum element in the input array
        m is the size of the count array

Space complexity    O(max)

Counting Sort algorithm runs depends on both the range of possible values k and the number of values n. In a best case
scenario, the range of possible different values k is very small compared to the number of values n and Counting Sort
has time complexity O(n)


[14, 46, 43, 27, 57, 41, 45, 21, 70]

Ascending order:    [14, 21, 27, 41, 43, 45, 46, 57, 70]
Descending order:   [70, 57, 46, 45, 43, 41, 27, 21, 14]

"""

from itertools import accumulate


def all_positives(lst: list[int]) -> bool:
    """Check whether all element in a list are positive integers"""
    return all(isinstance(_, int) and _ >= 0 for _ in lst)


def count_sort_out_of_place(lst: list[int], reverse: bool = False) -> list[...]:
    """A simple out-of-place implementation of count sort that works on lists of positive integers"""
    if not all_positives(lst):
        raise ValueError("Count sort works only on positives integers")

    # Initialize the output array
    res = []

    if not lst:
        return res

    # Initialize the count list
    count = [0] * (max(lst) + 1)

    # counting - items of the input array would be indices in the count array
    for _ in lst:
        count[_] += 1

    # get sorted output based on the counts
    r = [range(len(count)), range(len(count) - 1, -1, -1)][reverse]
    for i in r:
        while count[i]:
            res.append(i)
            count[i] -= 1

    return res



def count_sort(lst: list[int], reverse: bool = False) -> None:
    """Another implementation of count sort that uses the approach described in the docstring, and that works on lists
    of positive integers. While count sort is not an in-place sorting algorithm, this implementation brings extra over
    head by copying values from the auxiliary space to the input list, turning it to an in-place algorithm"""
    if not all_positives(lst):
        raise ValueError("count sort works only on positives integers")

    if not lst:
        return

    # Initialize the count list
    count = [0] * (max(lst) + 1)

    # Initialize the auxiliary array
    aux = [0] * len(lst)

    # counting - items of the input array would be indices in the count array
    for _ in lst:
        count[_] += 1

    # Get the cumulative sum of the counts - would help to calculate the index of items of the input list in the
    # auxiliary space
    if not reverse:
        count = list(accumulate(count))
    else:
        # the counts for descending order should be accumulated from right to left
        for i in range(len(count) - 2, -1, -1):
            count[i] += count[i + 1]

    # loop through the input list in reverse order to preserve the order of the identical items (stable algorithm)
    # calculate the position of items in the input list using the math described in the docstring above
    for i in range(len(lst) - 1, -1, -1):
        aux[count[lst[i]] - 1] = lst[i]
        count[lst[i]] -= 1

    # Copy the values from the auxiliary space to the input list to make it in-place approach
    # however you could abandon this step since its brings an extra overhead and make it an out-of-place method
    # Note: the whole point from this implementation is to implement the method described in the docstring
    for i, _ in enumerate(aux):
        lst[i] = _


def main():
    lst = [14, 46, 43, 27, 57, 41, 45, 21, 70]
    lst1 = lst[:]  # shallow copy

    count_sort(lst, False)
    print(lst)

    count_sort(lst1, True)
    print(lst1)


if __name__ == "__main__":
    main()
