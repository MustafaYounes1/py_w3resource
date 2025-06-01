"""

Write a Python program to check if two frozensets are disjoint (set has no elements in common with other).

{1, 2, 3, 4, 5}, {6, 7, 8}      =>  True
{1, 2, 3, 4}, {4, 5, 6, 7, 8}   =>  False

"""


def main():
    data = [
        [{1, 2, 3, 4, 5}, {6, 7, 8}],
        [{1, 2, 3, 4}, {4, 5, 6, 7, 8}]
    ]

    for a, b in data:
        print(frozenset(a).isdisjoint(b))


if __name__ == "__main__":
    main()
