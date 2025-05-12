"""

Write a Python program to sort unsorted numbers using Strand sort.

=========
Approach
=========
1. Start with an empty output list.
2. Extract the first strand (a sorted subsequence) from the input list.
    * Start from the first element of the input list.
    * Iterate through the list, and whenever an element is greater than or equal to the last added element in the
        strand, add it to the strand.
    * Remove the added elements from the input list
3. Merge this strand into the output list.
4. Repeat 2 & 3 until the output array holds a sorted version of the input array

Best Time Complexity:       O(n)
Average Time Complexity:    O(n^2)
Worst Time Complexity:      O(n^2)

Space Complexity:       O(n)    (Strand sort is not in-place)

[14, 46, 43, 27, 57, 41, 45, 21, 70]

Ascending order:    [14, 21, 27, 41, 43, 45, 46, 57, 70]
Descending order:   [70, 57, 46, 45, 43, 41, 27, 21, 14]

"""


def merge(lst1: list[...], lst2: list[...], reverse: bool) -> list[...]:
    """Merge two sorted lists into one bigger list"""
    res = []
    i = j = 0

    # would execute until both or one of the two input lists is totally consumed
    while (i < len(lst1)) and (j < len(lst2)):
        if [lst1[i] <= lst2[j], lst1[i] >= lst2[j]][reverse]:
            res.append(lst1[i])
            i += 1
        else:
            res.append(lst2[j])
            j += 1

    # Get the leftovers from lst1 if there are any
    res += lst1[i:]

    # Get the leftovers from lst2 if there are any
    res += lst2[j:]

    return res


def strand_sort(lst: list[...], reverse: bool = False) -> list[...]:
    """An implementation of Strand Sort"""
    res, visited = [], [False] * len(lst)

    while len(res) < len(lst):
        strand = []  # would hold a sorted subsequence extracted from the input list

        for i, item in enumerate(lst):
            # if the item was visited before => it got into one strand and merged with the output list -> skip it
            if visited[i]:
                continue

            # strand is empty -> build a new strand from the item at hand
            if not strand:
                strand.append(item)

            # strand holds items -> continue extracting sorted subsequences
            elif [item >= strand[-1], item <= strand[-1]][reverse]:
                strand.append(item)

            # doesn't belong to this strand -> do nothing
            else:
                continue

            # the item belongs to a strand now -> mark it as visited
            visited[i] = True

        # merge the output array with the extracted strand
        res = merge(res, strand, reverse)

    return res


def main():
    lst = [14, 46, 43, 27, 57, 41, 45, 21, 70]

    print(strand_sort(lst, False))
    print(strand_sort(lst, True))


if __name__ == "__main__":
    main()
