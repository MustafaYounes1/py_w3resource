"""

Write a Python program to check if a number is positive, negative or zero.

"""


def main():
    n = float(input("Enter a number: "))
    s = "positive" if n > 0 else "negative" if n < 0 else "zero"
    print(s)


if __name__ == "__main__":
    main()
