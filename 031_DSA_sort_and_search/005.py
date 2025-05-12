"""

Write a Python program to sort a list of elements using the insertion sort algorithm.

Insertion sort is a sorting algorithm that places an unsorted element at its suitable place in each iteration.

Insertion sort works the way we sort playing cards in our hands. We assume that the first card is already sorted then,
we select an unsorted card. If the unsorted card is greater than the card in hand, it is placed on the right otherwise,
to the left. In the same way, other unsorted cards are taken and put in their right place.

The algorithm uses one part of the array to hold the sorted values, and the other part of the array to hold values
that are not sorted yet. It takes one value at a time from the unsorted part of the array and puts it into the right
place in the sorted part of the array, until the array is sorted.

Worst Time Complexity:      O(n^2)
    If we want to sort in ascending order and the array is in descending order then the worst case occurs.

Average Time Complexity:    O(n^2)

Best Time Complexity:       O(n)
    If the array is already sorted

Space Complexity:   O(1)

[14, 46, 43, 27, 57, 41, 45, 21, 70]

Ascending order:    [14, 21, 27, 41, 43, 45, 46, 57, 70]
Descending order:   [70, 57, 46, 45, 43, 41, 27, 21, 14]

"""


def naive_insertion_sort(lst: list[...], reverse: bool = False) -> None:
    """A naive implementation of the insertion sort algorithm that suffers from a lot of memory shifting"""
    # consider the first value as the initial sorted part of the array.
    for i in range(1, len(lst)):
        curr_val = lst.pop(i)  # will cause shifting many elements to the left
        target_pos, j = i, i-1

        # navigate through the sorted part right to left and find the correct insertion position
        while j >= 0 and [lst[j] > curr_val, lst[j] < curr_val][reverse]:
            target_pos = j
            j -= 1

        lst.insert(target_pos, curr_val)  # will cause shifting many elements to the right


def insertion_sort(lst: list[...], reverse: bool = False) -> None:
    """An optimized implementation that don't shift a lot of elements by abandoning pop and insert"""
    for i in range(1, len(lst)):
        curr_val = lst[i]  # store the value of the current item
        target_pos, j = i, i-1

        # navigate through the sorted part right to left shifting items into the correct positions while trying to
        # find the correct position for the item in hand
        while j >= 0 and [lst[j] > curr_val, lst[j] < curr_val][reverse]:
            lst[j+1] = lst[j]
            target_pos = j
            j -= 1

        lst[target_pos] = curr_val


def main():
    lst = [14, 46, 43, 27, 57, 41, 45, 21, 70]
    lst1 = lst[:]  # shallow copy

    insertion_sort(lst, False)
    print(lst)

    insertion_sort(lst1, True)
    print(lst1)


if __name__ == "__main__":
    main()
