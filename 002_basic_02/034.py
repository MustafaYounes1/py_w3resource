"""

Write a Python program to check whether three given lengths (integers) of three sides form a right triangle.
Print "Yes" if the given sides form a right triangle otherwise print "No".

Integers separated by a single space.
1 <= length of the side <= 1,000

Input three integers(sides of a triangle)   8 6 7   -   3 4 5
                                            No      -   Yes

"""


def main():
    a, b, c = [int(_) for _ in input("Enter three space-separated integers: ").split()]
    if (pow(a, 2) + pow(b, 2)) == pow(c, 2):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
