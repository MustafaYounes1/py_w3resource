"""

Write a Python program to extract values from a given dictionary and create a list of lists from those values.

[
    {'student_id': 1, 'name': 'Jean Castro', 'class': 'V'},
    {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
    {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'},
    {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'},
    {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}
]


[
    [1, 'Jean Castro', 'V'],
    [2, 'Lula Powell', 'V'],
    [3, 'Brian Howell', 'VI'],
    [4, 'Lynne Foster', 'VI'],
    [5, 'Zachary Simon', 'VII']
]

"""


def main():
    data = [
        {'student_id': 1, 'name': 'Jean Castro', 'class': 'V'},
        {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
        {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'},
        {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'},
        {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}
    ]

    print(
        [list(d.values()) for d in data]
    )


if __name__ == "__main__":
    main()
