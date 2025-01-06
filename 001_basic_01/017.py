"""

Write a Python program to test whether a number is within 100 of 1000 or 2000.

"""


def main():
    n = int(input("Enter an integer number: "))
    if (abs(1000 - n) <= 100) or (abs(2000 - n) <= 100):
        print(f"{n} is within 100 of 1000 or 2000")
    else:
        print(f"{n} is not within 100 of 1000 or 2000")


if __name__ == "__main__":
    main()
