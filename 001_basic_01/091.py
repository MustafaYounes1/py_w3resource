"""

Write a Python program to swap two variables.

"""


def main():
    x = 1
    y = 2

    print(f"x={x}, y={y}")

    # using a tuple assignment
    x, y = y, x

    print(f"x={x}, y={y}")


if __name__ == "__main__":
    main()
