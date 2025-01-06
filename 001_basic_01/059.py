"""

Write a Python program to convert height (in feet and inches) to centimeters.

    1 foot = 30.48  cm
    1 inch = 2.54   cm

    1 foot = 12 inches
"""


def main():
    h_feet, h_inch = [float(_) for _ in input("Enter the height 'as h_in_feet h_in_inches': ").split()]
    print(f"Your height in cm: {h_feet * 30.48 + h_inch * 2.54}")


if __name__ == "__main__":
    main()
