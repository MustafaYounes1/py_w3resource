"""

Write a Python program that inputs a number and generates an error message if it is not a number.

"""


def main():
    try:
        n = int(input("Try not to input an integer: :) "))
        print(f"It is a number: {n}")

    except ValueError as err:
        print(err)


if __name__ == "__main__":
    main()
