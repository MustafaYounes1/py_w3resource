"""

Write a Python class named Student with the following private attributes: (name, age)
Create two instances student1 (Ben, 28), student2 (Mark, 29).
Print all the attributes of the student1, student2 instances with their values in the given format.

_Student__name Ben
_Student__age 28
**************************************************
_Student__name Mark
_Student__age 29
**************************************************

"""


class Student:
    def __init__(self, name:str, age:int):
        self.__name = name
        self.__age = age


def main():
    student1 = Student("Ben", 28)
    student2 = Student("Mark", 29)

    for student in (student1, student2):

        for attr in student.__dict__:
            print(attr, getattr(student, attr))

        print('*' * 50)


if __name__ == "__main__":
    main()
