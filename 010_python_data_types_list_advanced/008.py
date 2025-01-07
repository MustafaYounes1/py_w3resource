"""

Write a Python function to remove duplicates from a list while preserving the order.

[1, 2, 4, 3, 5, 4, 6, 9, 2, 1]                                          =>  [1, 2, 4, 3, 5, 6, 9]
['a', 'a', 'b', 'a', 'a', 'c', 'c', 'c', 'd', 'e', 'a', 'b', 'b', 'b']  =>  ['a', 'b', 'c', 'd', 'e']

"""


def main():
    data = [
        [1, 2, 4, 3, 5, 4, 6, 9, 2, 1],
        ['a', 'a', 'b', 'a', 'a', 'c', 'c', 'c', 'd', 'e', 'a', 'b', 'b', 'b']
    ]

    for lst in data:
        print([_ for idx, _ in enumerate(lst) if _ not in lst[:idx]])
        # or just use the ordered dictionary from the collections module
        # list(OrderedDict.fromkeys(lst))


if __name__ == "__main__":
    main()
