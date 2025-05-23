"""

Write a program to compute the radius and the central coordinate (x, y) of a circle which is constructed from three
given points on the plane surface.

Input:
x1, y1, x2, y2, x3, y3 separated by a single space.

Input three coordinate of the circle:       9 3 6 8 3 6
Radius of the said circle:                  3.358
Central coordinate (x, y) of the circle:    6.071 4.643

"""


def main():
    print("Input three coordinates of the circle:")
    x1, y1, x2, y2, x3, y3 = map(float, input().split())

    # Calculate distances between points
    c = (x1 - x2) ** 2 + (y1 - y2) ** 2
    a = (x2 - x3) ** 2 + (y2 - y3) ** 2
    b = (x3 - x1) ** 2 + (y3 - y1) ** 2

    # Calculate the cross-product
    s = 2 * (a * b + b * c + c * a) - (a ** 2 + b ** 2 + c ** 2)

    # Calculate the central coordinate of the circle
    px = (a * (b + c - a) * x1 + b * (c + a - b) * x2 + c * (a + b - c) * x3) / s
    py = (a * (b + c - a) * y1 + b * (c + a - b) * y2 + c * (a + b - c) * y3) / s

    # Calculate the radius of the circle
    ar = a ** 0.5
    br = b ** 0.5
    cr = c ** 0.5
    r = ar * br * cr / ((ar + br + cr) * (-ar + br + cr) * (ar - br + cr) * (ar + br - cr)) ** 0.5

    # Print the radius and central coordinate of the circle
    print("Radius of the said circle:")
    print("{:>.3f}".format(r))
    print("Central coordinate (x, y) of the circle:")
    print("{:>.3f}".format(px), "{:>.3f}".format(py))


if __name__ == "__main__":
    main()
