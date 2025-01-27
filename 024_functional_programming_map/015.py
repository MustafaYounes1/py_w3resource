"""

Write a Python program to split a given dictionary of lists into list of dictionaries using the map function.

marks = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}

[
    {'Science': 88, 'Language': 77},
    {'Science': 89, 'Language': 78},
    {'Science': 62, 'Language': 84},
    {'Science': 95, 'Language': 80}
]

"""


def main():
    marks = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
    print(list(map(dict, zip(*[[(key, v) for v in value] for key, value in marks.items()]))))


if __name__ == "__main__":
    main()
