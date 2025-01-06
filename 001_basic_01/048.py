"""

Write a Python program to parse a string to float or integer.

"""


def main():
    string = input("Enter a float number: ")

    # To a floating point number
    print(f"Float: {float(string)}")

    # Convert the floating-point number to an integer, truncating any decimal part, and print the result.
    print(f"Int: {int(float(string))}")


if __name__ == "__main__":
    main()
