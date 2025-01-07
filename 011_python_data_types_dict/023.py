"""

Write a Python program to combine values in a list of dictionaries.
Note: combine the values by linking the val of 'item' to the val of 'amount'

[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

{'item1': 1150, 'item2': 300}

"""

from collections import Counter
from functools import reduce
from operator import add


def main():
    data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
    print(
        dict(reduce(add, map(lambda d: Counter({d.get('item'): d.get('amount')}), data)))
    )


if __name__ == "__main__":
    main()
