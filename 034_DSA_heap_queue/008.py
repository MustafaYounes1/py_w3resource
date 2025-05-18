"""

Write a Python program to get the most expensive and least expensive items from a given dataset using the heap queue
algorithm.

items = [
    {'name': 'Item-1', 'price': 101.1},
    {'name': 'Item-2', 'price': 555.22},
    {'name': 'Item-3', 'price': 45.09},
    {'name': 'Item-4', 'price': 22.75},
    {'name': 'Item-5', 'price': 16.30},
    {'name': 'Item-6', 'price': 110.65}
]

First 3 expensive items:
[{'name': 'Item-2', 'price': 555.22},
 {'name': 'Item-6', 'price': 110.65},
 {'name': 'Item-1', 'price': 101.1}]

First 3 cheap items:
[{'name': 'Item-5', 'price': 16.3},
 {'name': 'Item-4', 'price': 22.75},
 {'name': 'Item-3', 'price': 45.09}]

"""

from heapq import nlargest, nsmallest
from operator import itemgetter


def main():
    items = [
        {'name': 'Item-1', 'price': 101.1},
        {'name': 'Item-2', 'price': 555.22},
        {'name': 'Item-3', 'price': 45.09},
        {'name': 'Item-4', 'price': 22.75},
        {'name': 'Item-5', 'price': 16.30},
        {'name': 'Item-6', 'price': 110.65}
    ]

    print(nlargest(3, items, key=itemgetter("price")))
    print(nsmallest(3, items, key=itemgetter("price")))


if __name__ == "__main__":
    main()
