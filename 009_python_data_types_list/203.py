"""

Write a Python program to join adjacent members of a given list.

['1', '2', '3', '4', '5', '6', '7', '8']
['12', '34', '56', '78']

['1', '2', '3']
['12']

"""


def main():
    data = [
        ['1', '2', '3', '4', '5', '6', '7', '8'],
        ['1', '2', '3']
    ]

    for lst in data:
        print([a + b for a, b in zip(lst[:-1:2], lst[1::2])])


if __name__ == "__main__":
    main()
