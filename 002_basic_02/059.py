"""

 A convex polygon is a simple polygon in which no line segment between two points on the boundary ever goes outside
 the polygon. Equivalently, it is a simple polygon whose interior is a convex set. In a convex polygon, all interior
 angles are less than or equal to 180 degrees, while in a strictly convex polygon all interior angles are strictly less
 than 180 degrees.

Write a Python program that compute the area of the polygon . The vertices have the names vertex 1, vertex 2, vertex 3,
 ... vertex n according to the order of edge connections

Note: The original sentences are uppercase letters, lowercase letters, numbers, symbols, less than 100 letters, and
consecutive letters are not more than 9 letters.

Hint: use the Triangle Formula from https://en.wikipedia.org/wiki/Shoelace_formula (abstract the result)
Input:

Input number of sides: 5
Side: 1
Input the Coordinate:
Input Coordinate x: 1
Input Coordinate y: 0
Side: 2
Input the Coordinate:
Input Coordinate x: 0
Input Coordinate y: 0
Side: 3
Input the Coordinate:
Input Coordinate x: 1
Input Coordinate y: 1
Side: 4
Input the Coordinate:
Input Coordinate x: 2
Input Coordinate y: 0
Side: 5
Input the Coordinate:
Input Coordinate x: -1
Input Coordinate y: 1
Area of the Polygon: 0.5

"""


def main():
    sides = int(input("Input number of vertices: "))
    vertices = []
    for _ in range(sides):
        vertices.append(
            [float(_) for _ in input("Enter the vertex coordinates x, y (space-separated): ").split()]
        )

    s = 0
    for idx in range(len(vertices) - 1):
        s += ((vertices[idx][0] * vertices[idx + 1][1]) - (vertices[idx + 1][0] * vertices[idx][1]))

    # last vertex and first index
    s += ((vertices[-1][0] * vertices[0][1]) - (vertices[0][0] * vertices[-1][1]))

    print(f"Area of the Polygon: {abs(s / 2):.2f}")


if __name__ == "__main__":
    main()
