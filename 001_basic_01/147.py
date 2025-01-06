"""

Write a Python function to check whether a number is divisible by another number. Accept two integer values
from the user.

"""


def main():
    x, y = [int(_) for _ in input("Enter two space-separated integers: ").split()]
    print(x % y == 0)


if __name__ == "__main__":
    main()
