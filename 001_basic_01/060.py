"""

Write a Python program to calculate the hypotenuse of a right-angled triangle.

A right triangle or right-angled triangle, or more formally an orthogonal triangle, is a triangle in which one angle
is a right angle. The relation between the sides and angles of a right triangle is the basis for trigonometry.
The side opposite the right angle is called the hypotenuse.

If the lengths of all three sides of a right triangle are integers, the triangle is said to be a Pythagorean triangle
and its side lengths are collectively known as a Pythagorean triple.

"""

import math


def main():
    s1, s2 = [float(_) for _ in input("Enter the sides lengths: 's1 s2' ").split()]
    print(f"The hypotenuse length: {math.sqrt(pow(s1, 2) + pow(s2, 2))}")


if __name__ == "__main__":
    main()
