"""

Write a Python program to calculate the difference between a given number and 17.
If the number is greater than 17, return twice the absolute difference.

"""


def main():
    n = int(input(f"Enter an integer number: "))
    if n > 17:
        print(abs(17 - n) * 2)
    else:
        print(17 - n)


if __name__ == "__main__":
    main()
