"""

Write a Python program to find the top k integers that occur the most frequently from a given list of integers using
the heap queue algorithm.

Note: If more than one element has same frequency then prioritise the larger element over the smaller one.

[3, 1, 4, 4, 5, 2, 6, 1], k = 2                 =>  [4, 1]
[7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9], k = 4     =>  [5, 11, 7, 10]

"""

from collections import Counter
from heapq import nlargest
from operator import itemgetter


def top_k_frequent(lst: list[int], k: int) -> list[int]:
    """Find the topK most frequent items in a given list"""
    counts = Counter(lst)

    return list(
        map(
            itemgetter(0),
            nlargest(k, counts.items(), key=itemgetter(1, 0))
        )
    )


def main():
   data = [
       ([3, 1, 4, 4, 5, 2, 6, 1], 2),
       ([7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9], 4)
   ]

   for lst, k in data:
       print(top_k_frequent(lst, k))


if __name__ == "__main__":
    main()
