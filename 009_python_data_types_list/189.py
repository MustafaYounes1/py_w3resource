"""

Write a Python program to shift last element to first position and first element to last position in a given list.

[1, 2, 3, 4, 5, 6, 7]
[7, 2, 3, 4, 5, 6, 1]

['s', 'd', 'f', 'd', 's', 's', 'd', 'f']
['f', 'd', 'f', 'd', 's', 's', 'd', 's']

"""


def main():
    data = [
        [1, 2, 3, 4, 5, 6, 7],
        ['s', 'd', 'f', 'd', 's', 's', 'd', 'f']
    ]

    for _ in data:
        _[0], _[-1] = _[-1], _[0]
        print(_)


if __name__ == "__main__":
    main()
