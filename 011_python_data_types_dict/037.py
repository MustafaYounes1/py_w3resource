"""

Write a Python program to replace dictionary values with their sums.
Note: Replace the keys 'V' and 'VI' with average and name it 'V+VI'

students = [
  {'id': 1, 'subject': 'math', 'V': 70, 'VI': 82},
  {'id': 2, 'subject': 'math', 'V': 73, 'VI': 74},
  {'id': 3, 'subject': 'math', 'V': 75, 'VI': 86}
]

[
    {'subject': 'math', 'id': 1, 'V+VI': 76.0},
    {'subject': 'math', 'id': 2, 'V+VI': 73.5},
    {'subject': 'math', 'id': 3, 'V+VI': 80.5}
]

"""


def main():
    students = [
        {'id': 1, 'subject': 'math', 'V': 70, 'VI': 82},
        {'id': 2, 'subject': 'math', 'V': 73, 'VI': 74},
        {'id': 3, 'subject': 'math', 'V': 75, 'VI': 86}
    ]

    for _ in students:
        _["V+VI"] = (_.pop("V") + _.pop("VI")) / 2

    print(students)


if __name__ == "__main__":
    main()
