"""

Write a Python program to sort a list of elements using shell sort algorithm.

Shell sort is mainly a variation of Insertion Sort. In insertion sort, we move elements only one position ahead.
When an element has to be moved far ahead, many movements are involved. The idea of ShellSort is to allow the exchange
of far items. Starting with far apart elements can move some out-of-place elements into position faster than a simple
nearest neighbor exchange.

Shell sort leverages the idea that inserting an element into a partially sorted array is more efficient than inserting
it into an entirely unsorted array.

It first sorts elements that are far apart from each other and successively reduces the interval between the
elements to be sorted. And when the gap becomes 1, Shell Sort essentially turns into Insertion Sort.

In brief, shell sort aims to improve Insertion Sort’s performance by partially sorting elements that are far apart
and gradually reducing the gap between elements to perform smaller and more efficient insertions. This allows Shell
Sort to take advantage of the partially sorted nature of the array and achieve faster sorting times.

=================
Choose a Sequence
=================

Shell Sort starts by selecting a sequence of intervals. The interval between the elements is to be sorted at each
pass reduced based on the sequence used.

Some of the optimal sequences that can be used in the shell sort algorithm are:
    Shell's original sequence:      N/2 , N/4 , …, 1
    Knuth's increments:             1, 4, 13, …, (3k – 1) / 2
    Sedgewick's increments:         1, 8, 23, 77, 281, 1073, 4193, 16577...4j+1+ 3·2j+ 1
    Hibbard's increments:           1, 3, 7, 15, 31, 63, 127, 255, 511…
    Papernov & Stasevich increment: 1, 3, 5, 9, 17, 33, 65,...
    Pratt:                          1, 2, 3, 4, 6, 9, 8, 12, 18, 27, 16, 24, 36, 54, 81....

===================================
Perform Insertion Sort on Sub lists
===================================

* performs Insertion Sort on a series of sub lists created by dividing the array based on the chosen increment sequence.
* Initially, the sub lists are items from the original list that are far apart from each other, and Insertion Sort
is performed on each sub list independently.
* As the algorithm progresses, the gap between elements decreases, and the sub lists would contain items that are closer
to each other.

====================
Gradually Reduce Gap
====================

* In each pass, the algorithm reduces the gap between elements by following the chosen sequence.
* Elements within each sub list are compared and swapped to partially sort them within their respective sub lists.

========================
Combine Sorted Sub lists
========================

* As the algorithm continues, the partially sorted sub lists begin to overlap.
* Eventually, the gap becomes 1, and the entire array is treated as a single sub list for the final pass.

==========
Final Pass
==========

* In the final pass, the gap is 1, effectively turning the algorithm into a regular Insertion Sort on the entire array.
* However, due to the previous passes, many elements are already partially sorted, leading to fewer comparisons and swaps.

The key idea behind Shell Sort is to strike a balance between the advantages of Insertion Sort (efficient for
partially sorted data) and the advantages of other sorting algorithms (efficient for larger datasets). By gradually
reducing the gap between elements, Shell Sort efficiently transforms the array into a state where elements are closer
to their final positions, reducing the number of comparisons and swaps required in the final pass.

The complexity depends on the interval chosen.

Worst Time Complexity:      O(n^2)
Average Time Complexity:    O(n * log n)
Best Time Complexity:       O(n * log n)

Space complexity:   O(1)

[14, 46, 43, 27, 57, 41, 45, 21, 70]

Ascending order:    [14, 21, 27, 41, 43, 45, 46, 57, 70]
Descending order:   [70, 57, 46, 45, 43, 41, 27, 21, 14]

"""

from typing import Generator


def shell_sequence(s: int) -> Generator[int, None, None]:
    """Implement the shell original sequence: n/2, n/4, n/8, ..., 1"""
    interval = s // 2
    yield interval

    interval //= 2
    while interval > 0:
        yield interval
        interval //= 2


def shell_sort(lst: list[...], reverse: bool = False) -> None:
    """Shell sort with the original shell sequence: n/2, n/4, n/8, ..., 1"""
    # perform insertion sort on all intervals/gaps: n/2, n/4, n/8, ..., 1 (when it's 1 => regular insertion sort)
    for interval in shell_sequence(len(lst)):

        # perform insertion sort on the current gap
        for i in range(interval, len(lst)):
            curr_val, j = lst[i], i

            while j >= interval and [lst[j - interval] > curr_val, lst[j - interval] < curr_val][reverse]:
                lst[j] = lst[j - interval]
                j -= interval

            lst[j] = curr_val


def main():
    lst = [14, 46, 43, 27, 57, 41, 45, 21, 70]
    lst1 = lst[:]  # shallow copy

    shell_sort(lst, False)
    print(lst)

    shell_sort(lst1, True)
    print(lst1)


if __name__ == "__main__":
    main()
