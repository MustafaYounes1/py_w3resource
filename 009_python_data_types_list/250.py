"""

Write a Python program to calculate the sum of a list, after mapping each element to a value using the provided
function.

[{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], v['n'] =>  20

"""

from operator import itemgetter


def main():
    lst = [{'n': 4}, {'n': 2}, {'n': 8}, {'n': 6}]
    print(sum(map(itemgetter('n'), lst)))


if __name__ == "__main__":
    main()
