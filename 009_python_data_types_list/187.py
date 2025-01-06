"""

Write a Python program to convert a given list of tuples to a list of strings.

[('red', 'green'), ('black', 'white'), ('orange', 'pink')]
['red green', 'black white', 'orange pink']

[('Laiba', 'Delacruz'), ('Mali', 'Stacey', 'Drummond'), ('Raja', 'Welch'), ('Saarah', 'Stone')]
['Laiba Delacruz', 'Mali Stacey Drummond', 'Raja Welch', 'Saarah Stone']

"""


def main():
    data = [
        [('red', 'green'), ('black', 'white'), ('orange', 'pink')],
        [('Laiba', 'Delacruz'), ('Mali', 'Stacey', 'Drummond'), ('Raja', 'Welch'), ('Saarah', 'Stone')]
    ]

    for _ in data:
        print([" ".join(__) for __ in _])


if __name__ == "__main__":
    main()
