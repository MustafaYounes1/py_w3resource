"""

Write a Python program to convert a dictionary into a list of lists.

{1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
[[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]

"""


def main():
    d = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
    print(list(map(list, d.items())))


if __name__ == "__main__":
    main()
