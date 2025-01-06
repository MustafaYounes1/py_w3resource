"""

Write a Python program to merge some list items in a given list using the index value.

['a', 'b', 'c', 'd', 'e', 'f', 'g']

Merge items from 2 to 4 in the said List:
['a', 'b', 'cd', 'e', 'f', 'g']

Merge items from 3 to 7 in the said List:
['a', 'b', 'c', 'defg']

"""


def main():
    lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    data = [
        (2, 4),
        (3, 7)
    ]

    for a, b in data:
        print(lst[:a] + ["".join(lst[a:b])] + lst[b:])


if __name__ == "__main__":
    main()
