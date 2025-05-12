"""

Write a Python program to sort unsorted numbers using Stooge sort.

Stooge Sort is a recursive sorting algorithm, known for its terrible time complexity. It is based on comparisons.

It generally divides the array into two overlapping parts (2/3 each). After that it performs sorting in first 2/3 part
and then it performs sorting in last 2/3 part. And then, sorting is done on first 2/3 part to ensure that the array is
sorted.

The key idea behind the first and last 2/3s is that, imagine for simplicity that you have three numbers: [4, 3, 1]
    * first step would sort the first 2/3 and put potential large elements within the reach of the next step
        sort 4 and 3    -> [3, 4, 1]      => (4 is within the reach of the second step)
    * second step would sort the last 2/3 and put the largest element at its correct place.
        sort 4 and 1    -> [3, 1, 4]
    * last step would take care of the remaining disorder in the first 2/3rd again
        sort 3 and 1    ->  [1, 3, 4]     =>  the list is sorted now

The same idea can be extended to bigger lists by applying the same approach recursively on each 2/3 part.

A nice illustration can be found in the first x minutes of the following YouTube Tutorial:

=========
Approach
==========
* first check the first and last elements of the list, and swap them if they are in the wrong order.
* If there are three or more elements in the list, then, the algorithm calls itself recursively on:
    * the initial 2/3 of the list
    * the final 2/3 of the list
    * and again on the initial 2/3 of the list, until all the list is sorted.

Note: always round down (floor) when calculating the third of the list size.

Its complexity is almost cubic, making it worse than Selection Sort or Insertion Sort.

Best/Average/Worst Time Complexity:     O(n^(log 3 / log 1.5)) = O(n^2.7095)
Space Complexity:                       O(n)

[14, 46, 43, 27, 57, 41, 45, 21, 70]

Ascending order:    [14, 21, 27, 41, 43, 45, 46, 57, 70]
Descending order:   [70, 57, 46, 45, 43, 41, 27, 21, 14]

"""


def __stooge_helper(lst: list[...], s: int, e: int, reverse: bool) -> None:
    """Stooge Sort Logic"""
    if s >= e:
        return

    # swap the first and last element if needed
    if [lst[s] > lst[e], lst[s] < lst[e]][reverse]:
        lst[s], lst[e] = lst[e], lst[s]

    # >= 3 elements
    if (e - s + 1) > 2:
        d = int((e - s + 1) / 3)  # round down when calculating the third of the list size
        __stooge_helper(lst, s, e - d, reverse)  # the first 2/3 part
        __stooge_helper(lst, s + d, e, reverse)  # the second 2/3 part
        __stooge_helper(lst, s, e - d, reverse)  # the first 2/3 part again


def stooge_sort(lst: list[...], reverse: bool = False) -> None:
    """An implementation of Stooge Sort"""
    __stooge_helper(lst, 0, len(lst) - 1, reverse)


def main():
    lst = [14, 46, 43, 27, 57, 41, 45, 21, 70]
    lst1 = lst[:]  # shallow copy

    stooge_sort(lst, False)
    print(lst)

    stooge_sort(lst1, True)
    print(lst1)


if __name__ == "__main__":
    main()
