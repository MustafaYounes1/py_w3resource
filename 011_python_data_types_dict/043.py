"""

Write a Python program to convert more than one list to a nested dictionary.

['S001', 'S002', 'S003', 'S004']
['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
[85, 98, 89, 92]

[
    {'S001': {'Adina Park': 85}},
    {'S002': {'Leyton Marsh': 98}},
    {'S003': {'Duncan Boyle': 89}},
    {'S004': {'Saim Richards': 92}}
]

"""


def main():
    lst1 = ['S001', 'S002', 'S003', 'S004']
    lst2 = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
    lst3 = [85, 98, 89, 92]

    print(
        {x: {y: z} for x, y, z in zip(lst1, lst2, lst3)}
    )


if __name__ == "__main__":
    main()
