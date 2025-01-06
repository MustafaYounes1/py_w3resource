"""

Write a Python program to calculate sum of digits of a number.

"""


def main():
    n = input("Enter a number: ")
    print(sum([int(_) for _ in n]))


if __name__ == "__main__":
    main()
