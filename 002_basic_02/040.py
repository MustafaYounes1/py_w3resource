"""

Write a Python program to check if a point (x,y) is in a triangle or not. A triangle is formed by three points.

"""


def main():
    # Prompt user to input coordinates of the triangle vertices (x1, y1), (x2, y2), (x3, y3),
    # and the point (xp, yp) to check if it lies inside the triangle
    print("Input x1, y1, x2, y2, x3, y3, xp, yp:")
    x1, y1, x2, y2, x3, y3, xp, yp = map(float, input().split())

    # Calculate the cross products (c1, c2, c3) for the point relative to each edge of the triangle
    c1 = (x2 - x1) * (yp - y1) - (y2 - y1) * (xp - x1)
    c2 = (x3 - x2) * (yp - y2) - (y3 - y2) * (xp - x2)
    c3 = (x1 - x3) * (yp - y3) - (y1 - y3) * (xp - x3)

    # Check if all cross products have the same sign (inside the triangle) or different signs (outside the triangle)
    if (c1 < 0 and c2 < 0 and c3 < 0) or (c1 > 0 and c2 > 0 and c3 > 0):
        print("The point is in the triangle.")
    else:
        print("The point is outside the triangle.")


if __name__ == "__main__":
    main()
