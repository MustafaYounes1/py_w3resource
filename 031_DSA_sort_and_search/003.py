"""

Write a Python program to sort a list of elements using the bubble sort algorithm.

According to Wikipedia "Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that
repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in
the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is
sorted.

The algorithm, which is a comparison sort, is named for the way smaller elements "bubble" to the top of the list.
Although the algorithm is simple, it is too slow and impractical for most problems even when compared to insertion sort.
It can be practical if the input is usually in sort order but may occasionally have some out-of-order elements nearly
in position."

Worst Time Complexity:      O(n^2)
    If we want to sort in ascending order and the array is in descending order then the worst case occurs.

Average Time Complexity:    O(n^2)

Best Time Complexity:       O(n)
    If the array is already sorted

Space Complexity:           O(1)

[14, 46, 43, 27, 57, 41, 45, 21, 70]

Ascending order:    [14, 21, 27, 41, 43, 45, 46, 57, 70]
Descending order:   [70, 57, 46, 45, 43, 41, 27, 21, 14]

"""


def bubble_sort(lst: list[...], reverse: bool = False) -> None:
    for i in range(len(lst) - 1):
        swapped = False

        for j in range(len(lst) - i - 1):
            if [lst[j] > lst[j + 1], lst[j] < lst[j + 1]][reverse]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True

        if not swapped:
            break


def main():
    lst = [14, 46, 43, 27, 57, 41, 45, 21, 70]
    lst1 = lst[:]  # shallow copy, alternatives: lst.copy(), list(copy), or copy.copy(list)

    bubble_sort(lst, False)
    print(lst)

    bubble_sort(lst1, True)
    print(lst1)


if __name__ == "__main__":
    main()