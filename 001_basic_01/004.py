"""

Write a Python program that calculates the area of a circle based on the radius entered by the user.

Sample Output :
===============
r = 1.1
Area = 3.8013271108436504

"""

import math


def main():
    r = float(input("Enter the circle radius: "))
    assert r > 0.0, "Expected a positive radius"
    print(f"The area of the circle: {math.pi * pow(r, 2)}")


if __name__ == "__main__":
    main()
