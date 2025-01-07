"""

Write a Python program to drop items with Nones as values from a given dictionary.

{'c1': 'Red', 'c2': 'Green', 'c3': None}

{'c1': 'Red', 'c2': 'Green'}

"""


def main():
    data = {'c1': 'Red', 'c2': 'Green', 'c3': None}
    print({k: v for k, v in data.items() if v is not None})


if __name__ == "__main__":
    main()
