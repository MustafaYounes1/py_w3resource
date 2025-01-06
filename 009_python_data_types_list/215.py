"""

Write a Python program to merge two or more lists into a list of lists, combining elements from each of the input
lists based on their positions.

['a', 'b'], [1, 2], [True, False]   =>  [['a', 1, True], ['b', 2, False]]
['a'], [1, 2], [True, False]        =>  [['a', 1, True], [None, 2, False]]
['a'], [1, 2], [True, False]        =>  [['a', 1, True], [None, 2, False]]

"""

from itertools import zip_longest


def main():
    data = [
        [['a', 'b'], [1, 2], [True, False]],
        [['a'], [1, 2], [True, False]],
        [['a'], [1, 2], [True, False]]
    ]

    for lst in data:
        print(list(zip_longest(*lst, fillvalue=None)))


if __name__ == "__main__":
    main()
