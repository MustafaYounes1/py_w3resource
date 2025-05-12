"""

Write a Python program to sort a list of elements using Pancake sort.

Pancake sorting is the colloquial term for the mathematical problem of sorting a disordered stack of pancakes in order
of size when a spatula can be inserted at any point in the stack and used to flip all pancakes above it.

A pancake number is the minimum number of flips required for a given number of pancakes.

The problem was first discussed by American geometer Jacob E. Goodman. It is a variation of the sorting problem in
which the only allowed operation is to reverse the elements of some prefix of the sequence.

Approach: Unlike a traditional sorting algorithm, which attempts to sort with the fewest comparisons possible,
the goal is to sort the sequence in as few reversals as possible.

"The idea is to do something similar to Selection Sort. We one by one place maximum element at the end and reduce the
size of current array by one."

Given an unsorted array, the task is to sort the given array. However, you are allowed to do only following operation
on array:
    flip(arr, i): Reverse array from 0 to i

* Let the current size be curr_size
* Start from curr_size equal to n and reduce curr_size by one while it’s greater than 1.
* Do following for every curr_size
    * Find index of the maximum element in arr[0 to curr_size-1]. Let the index be ‘mi’
    * Call flip(arr, mi)            => the maximum element would be at the first index
    * Call flip(arr, curr_size – 1) => the maximum element would be in its correct index

See following video for visualization of the above algorithm: https://www.youtube.com/watch?v=kk-_DDgoXfk

Worst/Average/Best Time Complexity: O(n^2)
Space Complexity:                   O(1)

[14, 46, 43, 27, 57, 41, 45, 21, 70]

Ascending order:    [14, 21, 27, 41, 43, 45, 46, 57, 70]
Descending order:   [70, 57, 46, 45, 43, 41, 27, 21, 14]

"""

from operator import itemgetter


def argmax(lst: list[...]) -> int:
    """Find the index of the largest element"""
    return max(enumerate(lst), key=itemgetter(1))[0]


def argmin(lst: list[...]) -> int:
    """Find the index of the smallest element"""
    return min(enumerate(lst), key=itemgetter(1))[0]


def flip(lst: list[...], idx: int) -> None:
    """Implement the only allowed operation, i.e., reverse array from 0 to idx
    e.g. when idx=1: [2, 1, 3] -> [1, 2, 3]"""
    assert idx < len(lst), f"{idx} exceeds the list bounds"
    lst[:idx+1] = lst[:idx+1][::-1]


def pancake_sort(lst: list[...], reverse: bool = False) -> None:
    """An implementation of Pancake Sort"""
    curr_size = len(lst)

    while curr_size > 1:
        if reverse:
           target_idx = argmin(lst[:curr_size])
        else:
            target_idx = argmax(lst[:curr_size])

        # if the target element is not already in its correct position
        if target_idx != (curr_size - 1):

            # Move the target element to the index 0 if it's not already there
            if target_idx != 0:
                flip(lst, target_idx)

            # Move the target element to its correct position
            flip(lst, curr_size - 1)

        curr_size -= 1


def main():
    lst = [14, 46, 43, 27, 57, 41, 45, 21, 70]
    lst1 = lst[:]  # shallow copy

    pancake_sort(lst, False)
    print(lst)

    pancake_sort(lst1, True)
    print(lst1)


if __name__ == "__main__":
    main()
