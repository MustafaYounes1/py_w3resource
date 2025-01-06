"""

Write a Python program to check if a triangle is equilateral, isosceles or scalene.
Note :
An equilateral triangle is a triangle in which all three sides are equal.
A scalene triangle is a triangle that has three unequal sides.
An isosceles triangle is a triangle with (at least) two equal sides.
Expected Output:

Input lengths of the triangle sides:
x: 6
y: 8
z: 12
Scalene triangle

"""


def main():
    a, b, c = list(map(int, input("Enter the lengths of the sides white-separated: ").split()))

    if a == b == c:
        print('equilateral triangle')

    elif a == b or b == c or a == c:
        print('isosceles triangle')

    else:
        print("scalene triangle")


if __name__ == "__main__":
    main()
