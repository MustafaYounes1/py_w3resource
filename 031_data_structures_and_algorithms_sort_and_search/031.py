"""

Write a Python program to sort an odd-even sort or odd-even transposition sort.

From Wikipedia: In computing, an odd-even sort or odd-even transposition sort (also known as brick sort
or parity sort  is a relatively simple sorting algorithm, developed originally for use on parallel processors
with local interconnections. It is a comparison sort related to bubble sort, with which it shares many characteristics.

It functions by comparing all odd/even indexed pairs of adjacent elements in the list and, if a pair is in the wrong
order (the first is larger than the second) the elements are switched. The next step repeats this for even/odd indexed
pairs (of adjacent elements). Then it alternates between odd/even and even/odd steps until the list is sorted.

========
Approach
========
* The algorithm runs until the array elements are sorted.

* In each iteration two phases occurs: Odd and Even Phases.

* In the odd phase, we perform a bubble sort on odd indexed elements and in the even phase, we perform a bubble sort
    on even indexed elements:
    Odd phase: Every odd indexed element is compared with the next even indexed element.
    Even phase: Every even indexed element is compared with the next odd indexed element.

A nice illustration of the algorithm can be found in this YouTube Tutorial: https://www.youtube.com/watch?v=1UEWb_dgkq8

Worst Time Complexity:      O(n^2)
Average Time Complexity:    O(n^2)
Best Time Complexity:       O(n)

Space Complexity:           O(1)

[14, 46, 43, 27, 57, 41, 45, 21, 70]

Ascending order:    [14, 21, 27, 41, 43, 45, 46, 57, 70]
Descending order:   [70, 57, 46, 45, 43, 41, 27, 21, 14]

"""


def odd_even_sort(lst: list[...], reverse: bool = False) -> None:
    """An implementation of Odd-Even Sort"""
    sorted_ = False
    start_indices = [1, 0]  # the current phase: 1 -> odd, 0 -> even

    while not sorted_:
        sorted_ = True

        # odd-phase: loop through odd indices and compare the values stored at them with the following items
        # even-phase: loop through even indices and compare the values stored at them with the following items
        for _ in start_indices:
            for i in range(_, len(lst) - 1, 2):
                if [lst[i] > lst[i + 1], lst[i] < lst[i + 1]][reverse]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
                    sorted_ = False


def main():
    lst = [14, 46, 43, 27, 57, 41, 45, 21, 70]
    lst1 = lst[:]  # shallow copy, alternatives: lst.copy(), list(copy), or copy.copy(list)

    odd_even_sort(lst, False)
    print(lst)

    odd_even_sort(lst1, True)
    print(lst1)

if __name__ == "__main__":
    main()
