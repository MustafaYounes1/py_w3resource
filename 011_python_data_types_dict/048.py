"""

Write a Python program to remove a specified dictionary from a given list.

[
    {'id': '#FF0000', 'color': 'Red'},
    {'id': '#800000', 'color': 'Maroon'},
    {'id': '#FFFF00', 'color': 'Yellow'},
    {'id': '#808000', 'color': 'Olive'}
]

Remove id #FF0000 from the said list of dictionary:

[
    {'id': '#800000', 'color': 'Maroon'},
    {'id': '#FFFF00', 'color': 'Yellow'},
    {'id': '#808000', 'color': 'Olive'}
]

"""


def main():
    data = [
        {'id': '#FF0000', 'color': 'Red'},
        {'id': '#800000', 'color': 'Maroon'},
        {'id': '#FFFF00', 'color': 'Yellow'},
        {'id': '#808000', 'color': 'Olive'}
    ]

    for idx, _ in enumerate(data):
        if _['id'] == "#FF0000":
            del data[idx]

    print(data)


if __name__ == "__main__":
    main()
