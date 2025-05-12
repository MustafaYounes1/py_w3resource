"""

Write a Python program to sort a list of elements using Comb sort.

The Comb Sort is a variant of the Bubble Sort.

Like the Shell sort, the Comb Sort increases the gap used in comparisons and exchanges. The basic idea is to eliminate
turtles, or small values near the end of the list, since in a bubble sort these slow the sorting down tremendously.
Rabbits, large values around the beginning of the list do not pose a problem in bubble sort.

In bubble sort, when any two elements are compared, they always have a gap of 1. The basic idea of comb sort is that
the gap can be much more than 1. The gap starts with a large value (typically len(lst) / 1.3) and shrinks by a
factor of 1.3 in every iteration until it reaches the value 1 (turning it to the regular bubble sort)

Note: The shrink factor has been empirically found to be 1.3 (by testing Comb sort on over 200,000 random lists)

============================
Improvement over Bubble Sort
============================
Bubble sort always compares adjacent values. So all inversions are removed one by one. Thus Comb Sort removes more than
one inversion with one swap and performs better than Bubble Sort.

Worst Time Complexity:      O(n^2)
Average Time Complexity:    O(n^2 / 2^p), where p is the number of increments
Best Time Complexity:       O(n * log n)

Space Complexity:           O(1)

[14, 46, 43, 27, 57, 41, 45, 21, 70]

Ascending order:    [14, 21, 27, 41, 43, 45, 46, 57, 70]
Descending order:   [70, 57, 46, 45, 43, 41, 27, 21, 14]

"""


def comb_sort(lst: list[...], reverse: bool = False, shrink_factor: float = 1.3) -> None:
    completed, gab = False, len(lst)

    # Keep running until the gab is 1 and no swap was performed
    while not completed:
        gab = max(1, int(gab / shrink_factor))  # make sure that the least value 'gab' would get is 1

        # if gab is 1 already, the algo could terminate, unless there is a need to swap adjacent elements
        if gab == 1:
            completed = True

        # perform bubble sort with gabs that diminish until 1 and would keep executing until no swap is performed
        for i in range(len(lst) - gab):
            if [lst[i] > lst[i + gab], lst[i] < lst[i + gab]][reverse]:
                lst[i], lst[i + gab] = lst[i + gab], lst[i]
                completed = False  # performing a swap would let the algorithm continue even if the gab is one already


def main():
    lst = [14, 46, 43, 27, 57, 41, 45, 21, 70]
    lst1 = lst[:]  # shallow copy

    comb_sort(lst, False)
    print(lst)

    comb_sort(lst1, True)
    print(lst1)


if __name__ == "__main__":
    main()
