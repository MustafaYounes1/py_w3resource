"""

Write a Python program to find the student with the second-lowest grade.
Note: Try to represent students as named-tuples

[['Avik Das ', 89.0], ['ayan Roy', 75.0], ['Sayan Dutta', 93.0]]

=>  Avik Das  89.0

"""

from collections import namedtuple
from operator import itemgetter


def main():
    lst = [['Avik Das ', 89.0], ['ayan Roy', 75.0], ['Sayan Dutta', 93.0]]
    Student = namedtuple("Student", "name grade", defaults=["fn ln", 0.0])
    sorted_data = sorted(map(lambda _: Student(*_), lst), key=itemgetter(1))
    target = sorted_data[1]
    print(target.name, target.grade)


if __name__ == "__main__":
    main()
