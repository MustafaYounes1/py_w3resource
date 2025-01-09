"""

Write a Python program to invert a dictionary with unique hashable values.

students = {
    'Theodore': 10,
    'Mathew': 11,
    'Roxanne': 9,
}

{10: 'Theodore', 11: 'Mathew', 9: 'Roxanne'}

"""


def main():
    students = {
        'Theodore': 10,
        'Mathew': 11,
        'Roxanne': 9,
    }
    print({v: k for k, v in students.items()})


if __name__ == "__main__":
    main()
