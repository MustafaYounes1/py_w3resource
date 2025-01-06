"""

Write a Python program to find common elements in a given list of lists.

[[7, 2, 3, 4, 7], [9, 2, 3, 2, 5], [8, 2, 3, 4, 4]]
[2, 3]

[['a', 'b', 'c'], ['b', 'c', 'd'], ['c', 'd', 'e']]
['c']

"""


def main():
    data = [
        [[7, 2, 3, 4, 7], [9, 2, 3, 2, 5], [8, 2, 3, 4, 4]],
        [['a', 'b', 'c'], ['b', 'c', 'd'], ['c', 'd', 'e']]
    ]

    for _ in data:
        print(set.intersection(*map(set, _)))


if __name__ == "__main__":
    main()
