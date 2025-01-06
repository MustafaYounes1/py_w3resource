"""

Write a Python program to input two integers on a single line.

e.g.: 1 2   =>   x = 1, y = 2

"""


def main():
    x, y = [int(_) for _ in input("Enter two space-separated integers: ").split()]
    print(x, y)


if __name__ == "__main__":
    main()
