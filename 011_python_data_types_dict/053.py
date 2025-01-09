"""

Write a Python program to find the length of the dictionary values and map the values to their lengths.

{1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
{'red': 3, 'green': 5, 'black': 5, 'white': 5}

{'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
{'Austin Little': 13, 'Natasha Howard': 14, 'Alfred Mullins': 14, 'Jamie Rowe': 10}

"""


def main():
    data = [
        {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'},
        {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
    ]

    for d in data:
        print({v: len(v) for v in d.values()})


if __name__ == "__main__":
    main()
