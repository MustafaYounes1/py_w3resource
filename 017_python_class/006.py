"""

Define a Python function student that takes the following arguments: student_id, student_name, and student_class
and return a string representation of a student.

The function will print the ID of a student (student_id). If the user passes an argument student_name or student_class
the function will print the student name and class.

ID: 'SV12', Name: 'Jean Garner'
    Student ID: SV12, Student Name: Jean Garner


ID: 'SV12', Name: 'Jean Garner', class: 'V'
    Student ID: SV12, Student Name: Jean Garner, Class: V

"""


def student(student_id: str, **kwargs):
    """Returns a string representation of a student"""
    rep = f"Student ID: {student_id}"

    if "student_name" in kwargs:
        rep += f", Student Name: {kwargs['student_name']}"

    if "student_class" in kwargs:
        rep += f", Class: {kwargs['student_class']}"

    return rep


def main():
    print(student("SV12", student_name="Jean Garner"))
    print(student("SV12", student_name="Jean Garner", student_class="V"))


if __name__ == "__main__":
    main()
