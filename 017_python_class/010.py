"""

Write a Python class named Student with two class attributes student_id ('V10'), and student_name ('Jacqueline Barnett')

Add a new attribute student_class ('V')
Display the namespace of the class.
Now remove the student_name attribute and display the namespace of the class.

__module__ __main__
__annotations__ {'student_id': <class 'str'>, 'student_name': <class 'str'>}
student_id V10
student_name Jacqueline Barnett
__dict__ <attribute '__dict__' of 'Student' objects>
__weakref__ <attribute '__weakref__' of 'Student' objects>
__doc__ None
student_class V
**************************************************
__module__ __main__
__annotations__ {'student_id': <class 'str'>, 'student_name': <class 'str'>}
student_id V10
__dict__ <attribute '__dict__' of 'Student' objects>
__weakref__ <attribute '__weakref__' of 'Student' objects>
__doc__ None
student_class V

"""


class Student:
    student_id: str = "V10"
    student_name: str = "Jacqueline Barnett"


def main():
    Student.student_class = 'V'

    for k, v in Student.__dict__.items():
        print(k, v)

    print("*" * 50)

    del Student.student_name

    for k, v in Student.__dict__.items():
        print(k, v)


if __name__ == "__main__":
    main()
