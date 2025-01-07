"""

Write a Python program to get a dictionary from an object's fields.

Suppose that you have an object called Dummy that has 3 attributes:
    x = 1
    y = 2
    z = 3

And let it have a method called 'do_nothing' that just does nothing!

Create an instance of it and get a dictionary out of it

{'x': 1, 'y': 2, 'z': 3}

"""


class Dummy(object):
    def __init__(self):
        self.x = 1
        self.y = 2
        self.z = 3

    def do_nothing(self):
        pass


def main():
    d = Dummy()
    print(d.__dict__)


if __name__ == "__main__":
    main()
