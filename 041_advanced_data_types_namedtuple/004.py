"""

Write a Python program that defines a NamedTuple called Student with fields like name, age, and marks.

Student(name='Svetovid Borko', age=22, marks={'Math': 85, 'Science': 90, 'History': 78, 'English': 92, 'Art': 88})
Student(name='Mohan Balbino', age=22, marks={'Math': 75, 'Science': 82, 'History': 95, 'English': 88, 'Art': 90})
Student(name='Tacita Jerzy', age=21, marks={'Math': 92, 'Science': 87, 'History': 85, 'English': 78, 'Art': 91})

"""

from collections import namedtuple


def main():
    data = [
        ["Svetovid Borko", 22, {"Math": 85, "Science": 90, "History": 78, "English": 92, "Art": 88}],
        ["Mohan Balbino", 22, {"Math": 75, "Science": 82, "History": 95, "English": 88, "Art": 90}],
        ["Tacita Jerzy", 21, {"Math": 92, "Science": 87, "History": 85, "English": 78, "Art": 91}]
    ]

    student = namedtuple("Student", ["name", "age", "marks"])
    students = [student(*std_data) for std_data in data]

    for std in students:
        print(std)

if __name__ == "__main__":
    main()
