"""

Write a Python program to create groups of similar items from a given list.

['red_1', 'red_2', 'green_1', 'green_2', 'green_3', 'orange_1', 'orange_2']
[['red_1', 'red_2'], ['green_1', 'green_2', 'green_3'], ['orange_1', 'orange_2']]

['red_1', 'green-1', 'green_2', 'green_3', 'orange-1', 'orange_2']
[['red_1'], ['green-1'], ['green_2', 'green_3'], ['orange-1'], ['orange_2']]

"""

from itertools import groupby


def main():
    data = [
        ['red_1', 'red_2', 'green_1', 'green_2', 'green_3', 'orange_1', 'orange_2'],
        ['red_1', 'green-1', 'green_2', 'green_3', 'orange-1', 'orange_2']
    ]

    for lst in data:
        print([list(g) for k, g in groupby(lst, key=lambda _: _.split("_")[0])])


if __name__ == "__main__":
    main()
