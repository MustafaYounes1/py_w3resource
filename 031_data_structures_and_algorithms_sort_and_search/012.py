"""

Write a Python program to sort a list of elements using Gnome sort.

Gnome sort is a sorting algorithm originally proposed by Dr. Hamid Sarbazi-Azad (Professor of Computer Engineering at
Sharif University of Technology) in 2000 and called "stupid sort" (not to be confused with bogosort), and then later
on described by Dick Grune and named "gnome sort".

The algorithm always finds the first place where two adjacent elements are in the wrong order, and swaps them.
It takes advantage of the fact that performing a swap can introduce a new out-of-order adjacent pair only next to the
two swapped elements.

Gnome Sort also called Stupid sort is based on the concept of a Garden Gnome sorting his flower pots.

A garden gnome sorts the flower pots by the following method:
1. He looks at the flower pot next to him and the previous one; if they are in the right order he steps one pot forward,
otherwise he swaps them and steps one pot backwards.
2. If there is no previous pot (he is at the starting of the pot line), he steps forwards; if there is no pot next to him
(he is at the end of the pot line), he is done.

Worst TIme Complexity:      O(n^2)
Average Time Complexity:    O(n^2)
Best TIme Complexity:       O(n)

Space Complexity:           O(1)

[14, 46, 43, 27, 57, 41, 45, 21, 70]

Ascending order:    [14, 21, 27, 41, 43, 45, 46, 57, 70]
Descending order:   [70, 57, 46, 45, 43, 41, 27, 21, 14]

"""


def gnome_sort(lst: list[...], reverse: bool = False) -> None:
    """Implement the Gnome Sort swapping-based algorithm"""
    if len(lst) < 1:
        return

    idx = 1
    while idx < len(lst):
        if [lst[idx] < lst[idx - 1], lst[idx] > lst[idx - 1]][reverse]:
            lst[idx], lst[idx - 1] = lst[idx - 1], lst[idx]
            idx = max(1, idx - 1)
        else:
            idx += 1


def main():
    lst = [14, 46, 43, 27, 57, 41, 45, 21, 70]
    lst1 = lst[:]  # shallow copy

    gnome_sort(lst, False)
    print(lst)

    gnome_sort(lst1, True)
    print(lst1)


if __name__ == "__main__":
    main()
