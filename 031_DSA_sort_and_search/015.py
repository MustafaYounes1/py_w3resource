"""

Write a Python program to sort a list of elements using Cycle sort.

Cycle sort is an in-place, unstable sorting algorithm, a comparison sort that is theoretically optimal in terms of the
total number of writes to the original array, unlike any other in-place sorting algorithm. It drastically reduces the
amount of memory writes required to sort. If a value is already in the proper location, it is written zero times;
otherwise, it is written only once to the correct spot.

Cycle sort is particularly useful when sorting arrays containing elements with a small range of values. It was developed
by W. D. Jones and published in 1963. It is based on the idea that the permutation to be sorted can be factored into
cycles (Cycle decompositions), which can individually be rotated to give a sorted result, i.e. the Cycle Sort finds a
set of cycles to sort the list.

============================
Cycles / Cycle Decomposition
============================
(1, 3)      => 1 should be positioned at the location of 3, and 3 should be positioned in the location of 1
(7, 10, 2)  => 7 should be positioned at the location of 10, and 10 should be positioned in the location of 2,
                and 2 should be positioned at the location of 7

The basic intuition is that: the correct position for a certain element e is at "the number of elements that are equal
or less than e".

Cycle Sort is based on the idea that the array to be sorted can be divided into cycles (cycle decomposition).
Cycles can be visualized as a graph. We have n nodes and an edge directed from node i to node j if the element at i-th
index must be present at j-th index in the sorted array.

All the cycles are considered one by one. First, we'll look at the cycle that contains the first element.
We determine the right position of the first element and set it there, say j. We take the old value of arr[j] and
locate its right location; we repeat this process until all components of the current cycle are correctly positioned,
i.e., it stops when we return to the cycle's beginning point.

========================================
How to generate the cycle decompositions
========================================
1. Start with an unsorted array of n elements.
2. Initialize a variable, cycleStart, to 0.
3. For each element in the array, compare it with every other element to its right. If there are any elements that
    are smaller than the current element, increment cycleStart. (trying to determine the correct position for the
    current element)
4. If cycleStart is still 0 after comparing the first element with all other elements, move to the next element and
    repeat step 3.
5. Otherwise, swap the current element with the element at the found position. The cycle is then continued (3-5) until
    the current element returns to the beginning of the current cycle. And this would indicate the end of the current
    cycle. (After then, all elements in this decomposition would be in their correct positions in the sorted list)
6. Repeat steps 3-5 until all cycles have been completed.

A good explanation can be found in this YouTube Tutorial: https://www.youtube.com/watch?v=hX8seJh1cT0

One of the advantages of cycle sort is that it has a low memory footprint, as it sorts the array in-place and does not
require additional memory for temporary variables or buffers, and most importantly, it does the least number of memory
writings

However, it can be slow in certain situations, particularly when the input array has a large range of values.
Nonetheless, cycle sort remains a useful sorting algorithm in certain contexts, such as when sorting small arrays
with limited value ranges.

Worst/Average/Best Time Complexity:     O(n^2)
Space Complexity:                       O(1)

[14, 46, 43, 27, 57, 41, 45, 21, 70]

Ascending order:    [14, 21, 27, 41, 43, 45, 46, 57, 70]
Descending order:   [70, 57, 46, 45, 43, 41, 27, 21, 14]

"""


def cyclic_sort(lst: list[...], reverse: bool = False) -> None:
    # loop through possible cycles / cycle decompositions
    for c_idx in range(len(lst) - 1):
        curr_item = lst[c_idx]  # would store the current item that we are going to write at its correct position
        pos = c_idx  # would hold the position of the current item in the sorted list

        # Determine the correct position of the current item.
        # loop through items on the right to the current item and count numbers that are less than the current item
        for j in range(c_idx + 1, len(lst)):
            if [lst[j] < curr_item, lst[j] > curr_item][reverse]:
                pos += 1

        # if position equals to the cycle index -> the item is at its correct position
        if pos == c_idx:
            continue

        # move the current element past any of its duplicates; otherwise, an infinite loop might show up
        while lst[pos] == curr_item:
            pos += 1

        # perform a write - place the current item at its correct position and continue with the next item in the cycle
        curr_item, lst[pos] = lst[pos], curr_item

        # continue with the rest of the cycle - rotate the rest of the cycle until the beginning of the cycle has been
        # reached
        while pos != c_idx:
            pos = c_idx  # restart the position to the start of the cycle index to calculate the correct pos of the
            # next item in the cycle

            # loop through items on the right to the current item and count numbers that are less than the current item
            for j in range(c_idx + 1, len(lst)):
                if [lst[j] < curr_item, lst[j] > curr_item][reverse]:
                    pos += 1

            # move the current element past any of its duplicates; otherwise, an infinite loop might show up
            while lst[pos] == curr_item:
                pos += 1

            # now place the current item at its correct position and continue with the next item in the cycle
            if curr_item != lst[pos]:
                curr_item, lst[pos] = lst[pos], curr_item


def main():
    lst = [14, 46, 43, 27, 57, 41, 45, 21, 70]
    lst1 = lst[:]  # shallow copy

    cyclic_sort(lst, False)
    print(lst)

    cyclic_sort(lst1, True)
    print(lst1)


if __name__ == "__main__":
    main()
