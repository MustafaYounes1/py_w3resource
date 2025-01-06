"""

Write a Python program to get the frequency of elements in a given list of lists.

[[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]

{1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}

"""

from collections import Counter
from itertools import chain


def main():
    lst = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
    print(dict(Counter(list(chain.from_iterable(lst)))))


if __name__ == "__main__":
    main()
