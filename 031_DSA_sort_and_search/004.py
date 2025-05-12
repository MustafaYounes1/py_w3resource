"""

Write a Python program to sort a list of elements using the selection sort algorithm.

The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order)
from unsorted part and putting it at the beginning. It finds the minimum element’s index in the unsorted portion of
the array and swaps it with the current index’s element.

Time Complexity:
    Best	O(n^2)
    Average	O(n^2)
    Worst	O(n^2)

Space Complexity: O(1)

[14, 46, 43, 27, 57, 41, 45, 21, 70]

Ascending order:    [14, 21, 27, 41, 43, 45, 46, 57, 70]
Descending order:   [70, 57, 46, 45, 43, 41, 27, 21, 14]

"""


def selection_sort(lst: list[...], reverse: bool = False) -> None:
    for i in range(len(lst) - 1):
        target_idx = i  # will hold the index to the smallest_asc/largest_desc item in each iteration
        for j in range(i + 1, len(lst)):
            if [lst[j] < lst[target_idx], lst[j] > lst[target_idx]][reverse]:
                target_idx = j

        lst[i], lst[target_idx] = lst[target_idx], lst[i]


def main():
    lst = [14, 46, 43, 27, 57, 41, 45, 21, 70]
    lst1 = lst[:]  # shallow copy

    selection_sort(lst, False)
    print(lst)

    selection_sort(lst1, True)
    print(lst1)


if __name__ == "__main__":
    main()
