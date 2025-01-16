"""

Write a Python program to create a class and display the namespace of that class.

The class would represent a person which has:
    1. The following members:   id (private) age (protected) name (global)
    2. The following methods:   do_nothing


__module__ __main__
__doc__ Person class
__init__ <function Person.__init__ at 0x000001C9BF658B80>
do_nothing <function Person.do_nothing at 0x000001C9BF659940>
__dict__ <attribute '__dict__' of 'Person' objects>
__weakref__ <attribute '__weakref__' of 'Person' objects>

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
    for k, v in Person.__dict__.items():
        print(k, v)


if __name__ == "__main__":
    main()
