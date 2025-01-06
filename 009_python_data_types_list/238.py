"""

Write a Python program to calculate the average of a given list, after mapping each element to a value using the
provided function.

{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }, x['n']         =>  5.0
{ 'n': 10 }, { 'n': 20 }, { 'n': -30 }, { 'n': 60 }, x['n']    =>  15.0

"""

from operator import itemgetter
from statistics import mean


def main():
    data = [
        [{'n': 4}, {'n': 2}, {'n': 8}, {'n': 6}],
        [{'n': 10}, {'n': 20}, {'n': -30}, {'n': 60}]
    ]

    for lst in data:
        print(mean(map(itemgetter('n'), lst)))


if __name__ == "__main__":
    main()
