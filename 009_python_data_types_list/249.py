"""

Write a Python program to get the minimum value of a list, after mapping each element to a value using a given function.

[{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], v['n']    =>  2

"""

from operator import itemgetter


def main():
    lst = [{'n': 4}, {'n': 2}, {'n': 8}, {'n': 6}]
    print(min(map(itemgetter('n'), lst)))


if __name__ == "__main__":
    main()
