"""

Write Python code to create a program for Bitonic Sort.

A bitonic sequence is a sequence of elements {a0, a1, …, an-1} such that:
    (1) there exist an index i such as {a0,a1, …..ai} is monotonically increasing and {ai, …, an-1} is monotonically
        decreasing or
    (2) there exist a cyclic shift of indices so (1) is satisfied.

Notes:
    1. A sequence, sorted in increasing order is considered Bitonic with the decreasing part as empty. Similarly,
    decreasing order sequence is considered Bitonic with the increasing part as empty. Thus, A sequence of only two
    elements is always considered as a bitonic sequence (<4, 5>, <7, 2>)
    2. A rotation (cyclic shift) of the Bitonic Sequence is also bitonic.

〈1, 2, 4, 7, 6, 0〉 is a bitonic sequence, because it first increases and then decreases
〈8, 9, 2, 1, 0, 4〉 is another bitonic sequence, because it is a cyclic shift of 〈0, 4, 8, 9, 2, 1>

===========================
How does Bitonic Sort work?
===========================
Simple put, the algorithm works by forming a bitonic sequence and finally sorting it using two procedures:
    Bitonic Split and Bitonic Merge

Note: Bitonic sort requires the input list to have a size that is power of two. The procedure of bitonic sequence fails
if the number of elements is not in the aforementioned quantity precisely.

=============
Bitonic Split
=============
1. We keep dividing the sequence into two halves where the first half is going to be sorted in ascending order and the
second half is going to be sorted in descending order (crucial for maintaining the bitonic property). The base case for
this recursive spilt is having an input of size 1 (since every two-element sequence is a valid bitonic sequence)

2. Using Bitonic Merge, We concatenate the two halves in order to bring a larger bitonic sequence (of size (based on
the recursion level; deepest to highest) 2, 4, 8, 16, 32, ...) for the uplevel call, and the larger bitonic sort to
be created would be sorted in the order that is required by uplevel call

=============
Bitonic Merge
=============
1. The initial call for this merge would be on two one-element lists, and they would get combined to form a bigger half
of two elements for the uplevel call sorted in the required sorting order.

2. Based on the uplevel sorting order (it could be ascending or descending), we swap elements from the two halves
if necessary so we can bring a bigger sorted half to the uplevel call in the way the uplevel call requires the half
to be sorted.

3. However after this initial swapping, the combined halves that would form the bigger half for the uplevel is not
guaranteed to be sorted
    example:    let's assume that we have two halves sorted in the required order (asc for left, desc for right)
                first half      1, 4
                second half     8, 3
                and the uplevel call requires a bitonic sort of 4 elements sorted in asc order (a, a, a, a, d, d, d, d)
                so it can bring the left half of a bitonic sequence of 8 elements for its uplevel call
                initial sort: (1, 4), (8, 3)    =>  ((1 < 8) -> no swap), ((4 > 3) -> swap)
                                                =>  [1, 3, 8, 4]; as you can see it's not sorted in asc order

To guarantee that list is sorted in the required order for the uplevel call, we repeat the swapping procedure on each
half with the required sorting order:
                [1, 3, 8, 4]    =>  (1, 3)  => (1), (3) agrees with the required sorting order
                                =>  (8, 4)  => (8), (4) disagrees with the required sorting order   =>  (4, 8)
                and thus [1, 3, 8, 4] would end up being [1, 3, 4, 8] (sorted in the required asc order)

For better illustration and nice visualization of the algorithm, you can refer to this YouTube Tutorial:
https://www.youtube.com/watch?v=uEfieI0MumY&list=PLzZR2BJ8ICYu_832OWSsKtt76PCuxLNZ8&index=10

Note: Bitonic sort is a parallel algorithm. It's better for parallel implementation because we always compare
elements in a predefined sequence and the sequence of comparison doesn’t depend on data that needs to be sorted (allows
all operations at each stage to execute concurrently without dependencies) (in a list of 8 elements: the 0th element
would always be compared with the 5th, 1st with 6th, 2nd with 7th, ...). So, we can run this algorithm on multiple
processors to make the sorting exponentially faster. In brief, this algo shines when it can run on multiple processors.

Best/Average/Worst Time Complexity:                         O(n * (log n)^2)
When implemented on a parallel machine with p processors:   O(n/p * (log n)^2)
Space complexity:                                           O(n * (log n)^2)

[2, 10, 20, 30, 5, 5, 4, 3]

Ascending order:    [2, 3, 4, 5, 5, 10, 20, 30]
Descending order:   [30, 20, 10, 5, 5, 4, 3, 2]

"""

from enum import IntEnum
from math import log2


class SortingOrder(IntEnum):
    """Represent possible sorting orders: 0 as Ascending, 1 as Descending"""
    ASCENDING = 0
    DESCENDING = 1


def bitonic_merge(lst: list[...], s: int, count: int, order: SortingOrder) -> None:
    if count > 1:
        k = count // 2  # split the count into two halves

        # Initial swapping to form bigger half in the desired order from the two halves in hand
        for i in range(s, s + k):
            if [lst[i] > lst[i + k], lst[i] < lst[i + k]][order]:
                lst[i], lst[i + k] = lst[i + k], lst[i]

        # initial swap is not enough to make sure that provided sequence is sorted in the desired order
        bitonic_merge(lst, s, k, order)
        bitonic_merge(lst, s + k, k, order)


def bitonic_split(lst: list[...], s: int, count: int, order: SortingOrder) -> None:
    """Implement the bitonic split to create two halves that are bitonic sequences and merge them in the desired order"""
    if count > 1:
        k = count // 2  # split the count into two halves
        bitonic_split(lst, s, k, SortingOrder.ASCENDING)  # the first half should be sorted in ascending order
        bitonic_split(lst, s + k, k, SortingOrder.DESCENDING)  # the second half should be sorted in descending order
        bitonic_merge(lst, s, count, order)  # merge the two halves and form a bigger half in the desired order


def bitonic_sort(lst: list[...], reverse: bool = False) -> None:
    """Implement the serial variant of bitonic sort"""
    if not lst:
        return

    # check the size of the input list
    if not log2(len(lst)).is_integer():
        raise ValueError("The size of the input list should be a power of 2, otherwise, "
                         "Bitonic Sort won't work as expected.")

    bitonic_split(lst, 0, len(lst), SortingOrder(reverse))


def main():
    lst = [2, 10, 20, 30, 5, 5, 4, 3]
    lst1 = lst[:]  # shallow copy

    bitonic_sort(lst, False)
    print(lst)

    bitonic_sort(lst1, True)
    print(lst1)


if __name__ == "__main__":
    main()
