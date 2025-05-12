"""

Write a Python program to sort a list of elements using Randomized Bogosort.

Bogosort Also known as permutation sort, stupid sort, slow sort, shotgun sort or monkey sort, is a particularly
ineffective sorting algorithm based on the generation and test paradigm. The algorithm successively generates
permutations of its input until it finds one that is sorted. It is not useful for sorting, but may be used for
educational purposes, to contrast it with other more realistic algorithms.

Two versions of the algorithm exist: a deterministic version that enumerates all permutations until it hits a sorted
one, and a randomized version that randomly permutes its input. An analogy for the working of the latter version is to
sort a deck of cards, it would consist of checking if the deck were in order, and if it were not, one would throw the
deck into the air, pick the cards up at random, and repeat the process until the deck is sorted.

Bogosort:
1. Check whether the list is sorted or not, if sorted then return the sorted array.
2. Otherwise, generate a randomization of the numbers until the array is sorted.

Worst Time Complexity:      O(infinity) (the randomized unbounded)
Average Time Complexity:    O(n * n!)
Best Time Complexity:       O(n)

Space Complexity:      O(1)

[14, 46, 43, 27, 57, 41, 45, 21, 70]

Ascending order:    [14, 21, 27, 41, 43, 45, 46, 57, 70]
Descending order:   [70, 57, 46, 45, 43, 41, 27, 21, 14]

"""

from itertools import pairwise
import random


def is_sorted(lst: list[...], reverse: bool = False) -> bool:
    """Check whether the input list is sorted or not"""
    for a, b in pairwise(lst):
        if [a > b, a < b][reverse]:
            return False
    return True


def bogo_sort(lst: list[...], reverse: bool = False) -> None:
    """Implement the randomized version of BogoSort"""
    while not is_sorted(lst, reverse):
        random.shuffle(lst)


def main():
    lst = [14, 46, 43, 27, 57, 41, 45, 21, 70]
    lst1 = lst[:]  # shallow copy

    bogo_sort(lst, False)
    print(lst)

    bogo_sort(lst1, True)
    print(lst1)


if __name__ == "__main__":
    main()
