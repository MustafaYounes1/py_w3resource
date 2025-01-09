"""

check if a specific key and a value exist in a dictionary.

('student_id', 1)           =>  True
('name', 'Brian Howell')    =>  True
('class', 'VII')            =>  True
('class', 'I')              =>  False
('name', 'Brian Howelll')   =>  False
('student_id', 11)          =>  False

"""


def main():
    students = [
        {'student_id': 1, 'name': 'Jean Castro', 'class': 'V'},
        {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
        {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'},
        {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'},
        {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}
    ]

    data = [
        ('student_id', 1),
        ('name', 'Brian Howell'),
        ('class', 'VII'),
        ('class', 'I'),
        ('name', 'Brian Howelll'),
        ('student_id', 11),
    ]

    items = [_ for d in students for _ in d.items()]

    for item in data:
        print(item in items)


if __name__ == "__main__":
    main()
