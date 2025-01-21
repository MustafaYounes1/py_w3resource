"""

Write a Python program to create a person class. Include attributes like name, country and date of birth.
Implement a method to determine the person's age.

Person("Mustafa Younes", "Syria", "1-11-1996")

Age: xx years, and xx months, and xx days

"""

from datetime import date, datetime


class Person:
    def __init__(self, name: str, country: str, date_of_birth: str):
        self.__name: str = name
        self.__cty: str = country
        self.__dob: date = datetime.strptime(date_of_birth, "%d-%m-%Y").date()

    @property
    def age(self) -> str:
        td = datetime.now().date() - self.__dob
        y, ld = int(td.days / 365.25), int(td.days % 365.25)
        m, d = ld // 30, ld % 30
        return f"Age: {y} years, and {m} months, and {d} days"


def main():
    p = Person("Mustafa Younes", "Syria", "1-11-1996")
    print(p.age)


if __name__ == "__main__":
    main()
