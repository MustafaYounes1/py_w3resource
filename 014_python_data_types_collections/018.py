"""

Write a Python program to merge more than one dictionary into a single expression.

{'R': 'Red', 'B': 'Black', 'P': 'Pink'} {'G': 'Green', 'W': 'White'}
{'G': 'Green', 'W': 'White', 'R': 'Red', 'B': 'Black', 'P': 'Pink'}

{'R': 'Red', 'B': 'Black', 'P': 'Pink'} {'G': 'Green', 'W': 'White'} {'O': 'Orange', 'W': 'White', 'B': 'Black'}
{'O': 'Orange', 'W': 'White', 'B': 'Black', 'G': 'Green', 'R': 'Red', 'P': 'Pink'}

"""

from collections import ChainMap


def main():
    data = [
        [
            {'R': 'Red', 'B': 'Black', 'P': 'Pink'},
            {'G': 'Green', 'W': 'White'}
        ],
        [
            {'R': 'Red', 'B': 'Black', 'P': 'Pink'},
            {'G': 'Green', 'W': 'White'},
            {'O': 'Orange', 'W': 'White', 'B': 'Black'}
        ]
    ]

    for dicts in data:
        # Note, the iteration order of a ChainMap is determined by scanning the mappings last to first
        print(dict(ChainMap(*dicts)))


if __name__ == "__main__":
    main()
