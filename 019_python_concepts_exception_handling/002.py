"""

Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not
a valid integer.

"""


def main():
    try:
        n = int(input("Enter an integer: "))
        print(n)

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
