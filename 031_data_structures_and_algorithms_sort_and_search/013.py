"""

Write a Python program to sort a list of elements using Cocktail shaker sort.

One problem of bubble sort is that its running time badly depends on the initial order of the elements.
Considering sorting in ascending order, big elements (rabbits) go up fast, while small ones (turtles) go down very slow.

Turtle example:
Element {1} is a turtle; {2, 3, 4, 5, 1} is almost sorted, it takes O(n^2) iterations to sort this array.

Rabbit example.
Element {6} is a rabbit, {6, 1, 2, 3, 4, 5} is almost sorted too, but it takes O(n) iterations to sort it.

Cocktail shaker sort also known as bidirectional bubble sort, cocktail sort, shaker sort, ripple sort, or shuffle sort,
is a variation of bubble sort that is both a stable sorting algorithm and a comparison sort. The algorithm differs from
a bubble sort in that it sorts in both directions on each pass through the list. This sorting algorithm is only
marginally more difficult to implement than a bubble sort, and solves the problem of turtles in bubble sorts.

It provides only marginal performance improvements, and does not improve asymptotic performance; like the bubble sort,
it is not of practical interest (insertion sort is preferred for simple sorts), though it finds some use in education.

============
How it works
============
The Bubble sort algorithm always traverses elements from left and moves the largest element to its correct position
in the first iteration and second-largest in the second iteration and so on.

Cocktail Sort is a variation of Bubble sort. It traverses through a given array in both directions alternatively.

Each iteration of the algorithm is broken up into 2 stages:
1. The first stage loops through the array from left to right, just like the Bubble Sort. During the loop, adjacent
items are compared and if the value on the left is greater than the value on the right, then values are swapped.
At the end of the first iteration, the largest number will reside at the end of the array.

2. The second stage loops through the array in opposite direction. Starting from the item just before the most recently
sorted item, and moving back to the start of the array. Here also, adjacent items are compared and are swapped if
required. At the end of the first iteration, the smallest number will reside at the beginning of the array.

Worst Time Complexity:      O(n^2)
Average Time Complexity:    O(n^2)
Best Time Complexity:       O(n)

Space Complexity:           O(1)

[14, 46, 43, 27, 57, 41, 45, 21, 70]

Ascending order:    [14, 21, 27, 41, 43, 45, 46, 57, 70]
Descending order:   [70, 57, 46, 45, 43, 41, 27, 21, 14]

"""


def cocktail_shaker_sort(lst: list[...], reverse: bool = False) -> None:
    """Cocktail Shaker (Bidirectional Bubble Sort) implementation that solves the rabbit-turtle problem of naive
    bubble sort"""
    # it's enough for the outer loop to loop through half size of the list; after each iteration of this outer loop
    # the i-th largest number would be in its correct position and the i-th smallest number would be in its correct
    # position (in case of ascending order)
    for i in range(len(lst) // 2):
        swapped = False

        # forward loop - asc order: at the end of the loop, the i-th largest element would be in its correct position
        for j in range(i, len(lst) - 1 - i):
            if [lst[j] > lst[j + 1], lst[j] < lst[j + 1]][reverse]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True

        if not swapped:
            break

        swapped = False

        # backward loop - asc order: at the end of the loop, the i-th smallest element would be in its correct position
        for j in range(len(lst) - i - 2, i, -1):
            if [lst[j] < lst[j - 1], lst[j] > lst[j - 1]][reverse]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
                swapped = True

        if not swapped:
            break


def main():
    lst = [14, 46, 43, 27, 57, 41, 45, 21, 70]
    lst1 = lst[:]  # shallow copy

    cocktail_shaker_sort(lst, False)
    print(lst)

    cocktail_shaker_sort(lst1, True)
    print(lst1)


if __name__ == "__main__":
    main()
