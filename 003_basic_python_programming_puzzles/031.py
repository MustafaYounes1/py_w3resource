"""

Write a Python program to find the coordinates of a triangle with given side lengths.

Input:
[3, 4, 5]
Output:
[[0.0, 0.0], [3, 0.0], [3.0, 4.0]]

Input:
[5, 6, 7]
Output:
[[0.0, 0.0], [5, 0.0], [3.8, 5.878775382679628]]

"""


def triangle_coordinates(sides):
    # Sort the side lengths in ascending order and assign them to variables a, b, and c
    a, b, c = sorted(sides)

    # Calculate the semi-perimeter of the triangle
    s = sum(sides) / 2

    # Use Heron's formula to calculate the area of the triangle
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

    # Calculate the height of the triangle
    y = 2 * area / a

    # Calculate the x-coordinate of the third vertex using the Pythagorean theorem
    x = (c ** 2 - y ** 2) ** 0.5

    # Return the coordinates of the vertices of the triangle as a list of lists
    return [[0.0, 0.0], [a, 0.0], [x, y]]


def main():
    seq = list(map(int, input("Enter the sides lengths comma-separated: ").split(",")))
    print(triangle_coordinates(seq))


if __name__ == "__main__":
    main()
