"""

Write a Python program to sort a given dictionary by key.

color_dict = {
    'red': '#FF0000',
    'green': '#008000',
    'black': '#000000',
    'white': '#FFFFFF'
}

{'black': '#000000', 'green': '#008000', 'red': '#FF0000', 'white': '#FFFFFF'}

"""


def main():
    color_dict = {
        'red': '#FF0000',
        'green': '#008000',
        'black': '#000000',
        'white': '#FFFFFF'
    }

    print({k: color_dict[k] for k in sorted(color_dict)})


if __name__ == "__main__":
    main()
