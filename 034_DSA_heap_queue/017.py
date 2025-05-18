"""

Write a Python program to convert a list into a heap and print it as a tree-like data structure.

[1, 2, 3, 4, 7, 9, 10, 8, 16, 14]

                             1
              2                             3
       4              7              9              10
   8      16     14

"""

from heapq import heapify
from math import floor, log


def heap_2_str(heap: list[...], max_lvl_width = 60, fill = " ") -> str:
    """Tree-like string representation of a heap"""
    res = ""

    if not heap:
        return res

    last_lvl = -1
    for i, n in enumerate(heap):
        lvl = floor(log(i + 1, 2))  # row (tree level) index

        if lvl != last_lvl:
            res += '\n'

        n_nodes = 2 ** lvl  # number of nodes in the current lvl
        node_padding = floor(max_lvl_width / n_nodes)

        res += str(n).center(node_padding, fill)
        last_lvl = lvl

    return res.strip('\n')


def main():
    lst = [1, 2, 3, 4, 7, 9, 10, 8, 16, 14]
    heapify(lst)
    print(heap_2_str(lst))


if __name__ == "__main__":
    main()
