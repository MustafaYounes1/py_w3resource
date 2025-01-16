"""

Define a Python function student that takes the following arguments: student_id, student_name, and student_class
and return a string representation of a student.

When provided with (S122, 'Wilson Medina', 'VI'):

Student ID: S122
Student Name: Wilson Medina
Class: VI

"""


def student(student_id: str, student_name: str, student_class: str):
    """Returns a string representation of a student"""
    return f"Student ID: {student_id}\nStudent Name: {student_name}\nClass: {student_class}"


def main():
    print(student("S122", "Wilson Medina", "VI"))


if __name__ == "__main__":
    main()
