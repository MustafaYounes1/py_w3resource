"""

Write a Python program to get the maximum value of a list, after mapping each element to a value using a
given function.

[{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], v['n']  =>  8

"""

from operator import itemgetter


def main():
    lst = [{'n': 4}, {'n': 2}, {'n': 8}, {'n': 6}]
    print(max(map(itemgetter('n'), lst)))


if __name__ == "__main__":
    main()
