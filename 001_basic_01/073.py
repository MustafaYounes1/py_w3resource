"""

Write a Python program to calculate the midpoints of a line.

"""


def main():
    p1 = [float(_) for _ in input("Enter x and y for the first point (space-separated): ").split()]
    p2 = [float(_) for _ in input("Enter x and y for the second point (space-separated): ").split()]
    print(f"Mid point of the line between p1 and p2: {(p1[0] + p2[0]) / 2}, {(p1[1] + p2[1]) / 2}")


if __name__ == "__main__":
    main()
