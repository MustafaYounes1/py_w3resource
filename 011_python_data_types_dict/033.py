"""

Write a Python program to check if multiple keys exist in a dictionary.

student = {
  'name': 'Alex',
  'class': 'V',
  'roll_id': '2'
}

'class', 'name'     =>  True
'name', 'Alex'      =>  False
'roll_id', 'name'   =>  True

"""


def main():
    student = {
        'name': 'Alex',
        'class': 'V',
        'roll_id': '2'
    }

    data = [
        ('class', 'name'),
        ('name', 'Alex'),
        ('roll_id', 'name')
    ]

    for names in data:
        # For sets >= simply means that it has the same or more items. Ordering doesn't come into it.
        print(student.keys() >= set(names))


if __name__ == "__main__":
    main()
