"""

Write a Python program to sort unsorted numbers using Pigeonhole sorting.

Pigeonhole sorting is a sorting algorithm that is suitable for sorting lists of elements where the number of elements
(n) and the length of the range of possible key values (k) are approximately the same. It requires O(n + k) time.

It is similar to counting sort, but differs in that it "moves items twice: once to the bucket array and again to the
final destination, whereas counting sort builds an auxiliary array then uses the array to compute each item's final
destination and move the item there."


The pigeonhole algorithm works as follows:
1. Find minimum and maximum values in array. Let the minimum and maximum values be ‘min’ and ‘max’ respectively.
    Also find range as ‘max-min+1’.

2. Set up an array of initially empty “pigeonholes” the same size as of the range.

3. Visit each element of the array and then put each element in its pigeonhole.
    An element arr[i] is put in hole at index arr[i] – min.

4. Start the loop all over the pigeonhole array in order and put the elements from non- empty holes back into the
    original array.

Space Complexity:   O(k)  where k is the length of the range of possible key values.

[14, 46, 43, 27, 57, 41, 45, 21, 70]

Ascending order:    [14, 21, 27, 41, 43, 45, 46, 57, 70]
Descending order:   [70, 57, 46, 45, 43, 41, 27, 21, 14]

"""


def all_positive_integers(lst: list[int]):
    """Check whether a list consists only of positive integers"""
    return all(isinstance(_, int) and _ >= 0 for _ in lst)


def pigeon_hole_sort(lst: list[int], reverse: bool = False) -> None:
    """An implementation of PigeonHole sorting algorithm"""
    if not lst:
        return

    if not all_positive_integers(lst):
        raise ValueError("This implementation of PigeonHole Sort works only with positive integers")

    _min, _max = min(lst), max(lst)
    k = _max - _min + 1  # find the length of the range of possible keys / number of holes

    pigeon_holes = [0] * k  # initialize the pigeon holes

    # put the pigeons in their holes
    for pigeon in lst:
        pigeon_holes[pigeon - _min] += 1  # map the pigeon into its corresponding hole

    # Put the pigeons back into the array in order
    idx = 0
    for hole in [range(k), range(k - 1, -1, -1)][reverse]:
        count = pigeon_holes[hole]  # get the pigeon count in the current hole

        # while the hole isn't empty
        while count:
            lst[idx] = hole + _min  # map hole to pigeon
            count -= 1
            idx += 1


def main():
    lst = [14, 46, 43, 27, 57, 41, 45, 21, 70]
    lst1 = lst[:]  # shallow copy

    pigeon_hole_sort(lst, False)
    print(lst)

    pigeon_hole_sort(lst1, True)
    print(lst1)


if __name__ == "__main__":
    main()
