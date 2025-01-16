"""

Write a Python program to create two empty classes, Student and Marks.
Now create some instances and check whether they are instances of the said classes or not.
Also, check whether the said classes are subclasses of the built-in object class or not.

An instance of Student is of the 'Student' type: True
An instance of Student is of the 'object' type:  True
An instance of Marks is of the 'Student' type: True
An instance of Marks is of the 'object' type:  True

"""


class Student:
    pass


class Marks:
    pass


def main():
    s = Student()
    print(f"An instance of Student is of the 'Student' type: {isinstance(s, Student)}")
    print(f"An instance of Student is of the 'object' type:  {isinstance(s, object)}")

    m = Marks()
    print(f"An instance of Marks is of the 'Student' type: {isinstance(m, Marks)}")
    print(f"An instance of Marks is of the 'object' type:  {isinstance(m, object)}")




if __name__ == "__main__":
    main()
