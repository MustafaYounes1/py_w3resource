"""

Write a Python program that will accept the base and height of a triangle and compute its area.

"""


def main():
    inputs = [float(_) for _ in input("Enter the triangle base and height (space-separated): ").split()]
    base, height = inputs[0], inputs[1]
    print(0.5 * base * height)


if __name__ == "__main__":
    main()
