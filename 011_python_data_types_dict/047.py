"""

Write a Python program to split a given dictionary of lists into lists of dictionaries.

{'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}

[
    {'Science': 88, 'Language': 77},
    {'Science': 89, 'Language': 78},
    {'Science': 62, 'Language': 84},
    {'Science': 95, 'Language': 80}
]

"""


def main():
    data = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
    print(
        [dict(zip(data.keys(), vals)) for vals in zip(*data.values())]
    )


if __name__ == "__main__":
    main()
