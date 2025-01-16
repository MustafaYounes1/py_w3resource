"""


Write a Python class named Student with two class attributes: student_id ('V10'), student_name ('Jacqueline Barnett').
Create a function called display to show all attributes and their values in the Student class.

ID: V10, Name: Jacqueline Barnett

"""


class Student:
    student_id: str = "V10"
    student_name: str = "Jacqueline Barnett"


def display() -> None:
    print(f"ID: {Student.student_id}, Name: {Student.student_name}")


def main():
    display()


if __name__ == "__main__":
    main()
