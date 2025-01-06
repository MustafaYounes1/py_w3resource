"""

Write a Python program to test whether all numbers in a list are greater than a certain number.

"""


def main():
    seq = [int(_) for _ in input("Enter a list of space-separated integers: ").split()]
    n = int(input("Enter the integer: "))
    print(all(_ > n for _ in seq))


if __name__ == "__main__":
    main()
