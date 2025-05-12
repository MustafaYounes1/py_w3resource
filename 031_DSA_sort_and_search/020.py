"""

Write a Python program to sort unsorted numbers using TimSort.

From Wikipedia: Timsort is a hybrid stable sorting algorithm, derived from merge sort and insertion sort, designed to
perform well on many kinds of real-world data. It was implemented by Tim Peters in 2002 for use in the Python
programming language.

The algorithm finds subsequences of the data that are already ordered (runs) and uses them to sort the remainder more
efficiently. This is done by merging runs until certain criteria are fulfilled.

Timsort has been Python's standard sorting algorithm since version 2.3.

The way Timsort works can be grossly oversimplified as follows:
    1. Divide the data into small chunks/runs (he size of these runs usually varies between 32 and 64 items)
    2. Sort these chunks using Insertion sort
    3. Merge the sorted chunks using a smart merging strategy found in Merge sort

Note: TimSort brings out many optimizations over just naively merging Insertion Sort and Merge Sort, e.g.:
    1. minimum run size.
    2. Detecting ascending runs and use them as they are.
    3. Detecting descending runs and blindly reverse them.
    4. Binary Insertion Sort
    5. Galloping while merging.
    6. Adaptive merging.

For more details, please refer to: https://www.kirupa.com/sorts/timsort.htm

Best Time Complexity:       O(n)
Average ime Complexity:     O(n log(n))
Worst ime Complexity:       O(n log(n))

Space Complexity:           O(n)

However, for the sake of simplicity, you are tasked to implement the following approach:

1. Split the array into runs of predefined size.
2. Sort each run independently using Binary Insertion Sort.
3. Merge the sorted runs as follows:
    a. At each merging run, spilt the array into pairs of two consecutive sorted runs and merge each pair separately.
    b. The size of the sorted runs would initially be the same as the input run size, and at each step it would double.
    c. e.g.:    r1  |   r2  |   r3  |   r4      (Merge r1 & r2, Merge r3 & r4)
                   r1_r2     |     r3_r4        (Merge r1_r2 & r3_r4)
                        r1_r2_r3_r4             (The list is sorted now)

[14, 46, 43, 27, 57, 41, 45, 21, 70]

Ascending order:    [14, 21, 27, 41, 43, 45, 46, 57, 70]
Descending order:   [70, 57, 46, 45, 43, 41, 27, 21, 14]

"""


def binary_search(lst: list[...], s: int, e: int, item: ..., reverse: bool) -> int:
    """Find the target index to insert the provided item in the sorted part using Binary Search
    Ascending: this would be the index of the first element that is larger than the item to be inserted
    Descending: this would be the index of the first element that is smaller than the item to be inserted
    The sorted part of the array is bounded by the following closed range [s, e]
    """
    while s <= e:
        mid = s + (e - s) // 2

        # the algorithm should be stable
        if lst[mid] == item:
            return mid + 1

        elif [lst[mid] < item, lst[mid] > item][reverse]:
            s = mid + 1

        else:
            e = mid - 1

    return s


def binary_insertion_sort(lst: list[...], run_s: int, run_e: int, reverse: bool) -> None:
    """Sort a specific chunk/run that lies in the range [run_s, run_e[ using Binary Insertion Sort"""
    for i, item in enumerate(lst[run_s + 1: run_e], start=run_s + 1):
        j = i - 1

        # find the target index to insert the current item in this run's sorted part using Binary Search
        target_idx = binary_search(lst, run_s, j, item, reverse)

        # shift the elements in the sorted part to the right if needed before inserting the new item
        while j >= target_idx:
            lst[j + 1] = lst[j]
            j -= 1

        # put the current item at its target position in the sorted part of the current run
        lst[target_idx] = item


def merge(lst: list[...], first_run_s: int, run_size: int, reverse: bool) -> None:
    """Merge two consecutive sorted runs of predefined size given the index where the first run starts"""
    l_s, l_e = first_run_s, first_run_s + run_size
    r_s, r_e = first_run_s + run_size, first_run_s + 2 * run_size

    left = lst[l_s: l_e]
    right = lst[r_s: r_e]

    i = j = 0
    k = first_run_s

    # following loop would break once one half (or both halves) is totally consumed
    while i < len(left) and j < len(right):
        if [left[i] <= right[j], left[i] >= right[j]][reverse]:
            lst[k] = left[i]
            i += 1
            k += 1
        else:
            lst[k] = right[j]
            j += 1
            k += 1

    # get the leftovers from the left half if there are any
    if i < len(left):
        lst[k: r_e] = left[i:]

    # get the leftovers from the left half if there are any
    if j < len(right):
        lst[k: r_e] = right[j:]


def tim_sort(lst: list[...], reverse: bool = False, run_size: int = 4) -> None:
    """Naive Implementation of TimSort"""
    assert run_size > 0, "Invalid run size - expected a non-zero positive size"

    # sort each individual run using Binary Insertion Sort #
    for i in range(0, len(lst), run_size):
        binary_insertion_sort(lst, i, i + run_size, reverse)

    # Apply merging #
    # the initial size of the consecutive chunks to be merged would initially be the same as the algorithm run size,
    # since all chunks of this size were sorted in the previous step
    size = run_size

    while size <= len(lst):
        for i in range(0, len(lst), 2 * size):
            # Apply the merging on pairs of consecutive sorted runs to form a bigger sorted run from each pair and
            # use it in the next pass
            merge(lst, i, size, reverse)

        size *= 2


def main():
    lst = [14, 46, 43, 27, 57, 41, 45, 21, 70]
    lst1 = lst[:]  # shallow copy

    tim_sort(lst, False, 4)
    print(lst)

    tim_sort(lst1, True, 4)
    print(lst1)

if __name__ == "__main__":
    main()
