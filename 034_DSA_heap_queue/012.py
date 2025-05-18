"""

Write a Python program to get the k most frequent elements from a given non-empty list of words using the heap queue
algorithm

["a", "abc", "abcdef", "a", "abcd", "abcd", "abc", "abcdefg"], 3  =>  ['a', 'abc', 'abcd']

"""

from collections import Counter
from heapq import nlargest
from operator import itemgetter


def top_k_most_frequent(lst: list[str], k: int) -> list[str]:
    counts = Counter(lst)

    return list(
        map(
            itemgetter(0),
            nlargest(k, counts.items(), key=lambda p: (p[1], -len(p[0])))
        )
    )


def main():
    lst = ["a", "abc", "abcdef", "a", "abcd", "abcd", "abc", "abcdefg"]
    print(top_k_most_frequent(lst, 3))


if __name__ == "__main__":
    main()
