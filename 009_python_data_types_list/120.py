"""

Write a Python program to create a list taking alternate elements from a given list.

['red', 'black', 'white', 'green', 'orange']
['red', 'white', 'orange']

[2, 0, 3, 4, 0, 2, 8, 3, 4, 2]
[2, 3, 0, 8, 4]

"""


def main():
    data = [
        ['red', 'black', 'white', 'green', 'orange'],
        [2, 0, 3, 4, 0, 2, 8, 3, 4, 2]
    ]

    for _ in data:
        print(_[::2])


if __name__ == "__main__":
    main()
