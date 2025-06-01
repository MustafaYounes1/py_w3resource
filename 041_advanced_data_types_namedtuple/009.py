"""

Write a Python program that defines a NamedTuple named "Car" with fields 'make', 'model', 'year', and 'engine'
(a NamedTuple representing engine details: type and #cylinders).

Create an instance of the "Car" NamedTuple and print its attributes.

Car(make='Honda', model='City', year=2020, engine=Engine(type='1.5L', cylinders=4))

"""

from typing import NamedTuple


class Engine(NamedTuple):
    type: str
    cylinders: int


class Car(NamedTuple):
    make: str
    model: str
    year: int
    engine: Engine


def main():
    c = Car(make='Honda', model='City', year=2020, engine=Engine('1.5L', 4))
    print(c)


if __name__ == "__main__":
    main()
