"""

Write a Python program that defines a NamedTuple called Point with fields x, y and z representing the coordinate of a
point. Access and print the fields.

x: 0, y: 0, z: 0
x: 1, y: 1, z: 2

"""

from collections import namedtuple


def main():
    point = namedtuple("Point", "x y z", defaults=[0, 0, 0])

    p0 = point()
    p1 = point(1, 1, 2)

    for p in (p0, p1):
        print(f"x: {p.x}, y: {p.y}, z: {p.z}")


if __name__ == "__main__":
    main()
