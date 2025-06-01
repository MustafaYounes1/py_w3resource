"""

Write a Python program that creates a 'Counter' for a list of items and uses dictionary-style access to update the
count of specific items.

items = ['Red', 'Green', 'Black', 'Black', 'Red', 'Red', 'Orange', 'Pink', 'Pink', 'Red', 'White']

subtract 2 from the "Red" count and add 1 to the "purple" count:

-> Counter({'red': 2, 'black': 2, 'pink': 2, 'green': 1, 'orange': 1, 'white': 1, 'purple': 1})

"""

from collections import Counter


def main():
    items = ['Red', 'Green', 'Black', 'Black', 'Red', 'Red', 'Orange', 'Pink', 'Pink', 'Red', 'White']
    c = Counter(map(lambda w: w.lower(), items))

    c["red"] -= 2
    c["purple"] += 1

    print(c)


if __name__ == "__main__":
    main()
