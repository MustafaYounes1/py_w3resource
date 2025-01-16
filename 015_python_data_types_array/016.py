"""

Write a Python program to check whether a list follows the sequence given in a pattern unicode array.

list                                pattern
["red", "green", "green", "red"],   ["a", "b", "b", "a"]        =>  True
["red", "green", "greenn"],         ["a", "b", "b"]             =>  False

"""

from array import array
from collections import defaultdict


def main():
    data = [
        [["red", "green", "green", "red"], array('u', ["a", "b", "b", "a"])],
        [["red", "green", "greenn"], array('u', ["a", "b", "b"])]
    ]

    for lst, pat in data:
        mapping = defaultdict(list)

        for idx, u_char in enumerate(pat):
            mapping[u_char].append(idx)

        print(all(len(set([lst[_] for _ in __])) == 1 for __ in mapping.values()))


if __name__ == "__main__":
    main()
