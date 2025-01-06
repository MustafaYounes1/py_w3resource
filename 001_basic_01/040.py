"""

Write a Python program to calculate the Euclidean Distance between the points (x1, y1) and (x2, y2).

"""

import math


def main():
    p1 = [float(_) for _ in input("Enter x and y for the first point (space-separated): ").split()]
    p2 = [float(_) for _ in input("Enter x and y for the second point (space-separated): ").split()]
    dst = math.sqrt(pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2))
    print(dst)


if __name__ == "__main__":
    main()
