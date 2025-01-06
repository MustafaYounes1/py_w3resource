"""

Write a Python program to convert the distance (in feet) to inches, yards, and miles.

    1 inch = 2.54   cm
    1 foot = 12   inch
    1 yard = 3    feet
    1 yard = 36   inch
    1 mile = 1760 yards
    1 mile = 5280 feet

"""


def main():
    feet = float(input("Enter the distance in feet: "))
    print(f"Distance in inches: {feet * 12}")
    print(f"Distance in yards: {feet / 3: 4f}")
    print(f"Distance in miles: {feet / 5_280: 4f}")


if __name__ == "__main__":
    main()
