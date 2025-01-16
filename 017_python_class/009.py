"""

Write a Python class named Student with two class attributes student_name ("Mustafa"), mark (93).
Modify the attribute values of the said class ("Younes", 100)
Print the original and modified values of the said attributes.

Original name: Mustafa
Original mark: 93
Modified name: Younes
Modified mark: 100

"""


class Student:
    name: str = "Mustafa"
    mark: int = 93


def main():
    print(f"Original name: {getattr(Student, 'name')}")
    print(f"Original mark: {getattr(Student, 'mark')}")

    setattr(Student, "name", "Younes")
    setattr(Student, "mark", 100)

    print(f"Modified name: {getattr(Student, 'name')}")
    print(f"Modified mark: {getattr(Student, 'mark')}")


if __name__ == "__main__":
    main()
