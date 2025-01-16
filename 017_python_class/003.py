"""

Write a Python program to create an instance of a specified class and display the namespace of the said instance.

The class would represent a person which has:
    1. The following members:   id (private) age (protected) name (global)
    2. The following methods:   do_nothing

The instance would have the following info: ("Mustafa" as the name, 1 as the id, and 28 as the age)

{'_Person__pid': 0, '_age': 28, 'name': 'Mustafa'}

"""


class Person:
    """Person class"""
    def __init__(self, pid=0, age=0, name="fn ls"):
        self.__pid = 0
        self._age = age
        self.name = name

    def do_nothing(self):
        pass


def main():
    p = Person(1, 28, "Mustafa")
    print(p.__dict__)


if __name__ == "__main__":
    main()
