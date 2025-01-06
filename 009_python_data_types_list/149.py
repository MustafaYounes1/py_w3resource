"""

Write a Python program to get all possible combinations of the elements of a given list.

['orange', 'red', 'green', 'blue']

[
    [], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'],
    ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'],
    ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']
]

"""

from itertools import combinations


def main():
    lst = ['orange', 'red', 'green', 'blue']

    print([_ for i in range(len(lst) + 1) for _ in list(combinations(lst, i))])


if __name__ == "__main__":
    main()
