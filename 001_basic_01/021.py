"""

Write a Python program that determines whether a given number (accepted from the user) is even or odd,
and prints an appropriate message to the user.

"""


def main():
    n = int(input("Enter a number: "))
    if n % 2 == 0:
        print(f"{n} is an even number")
    else:
        print(f"{n} is an odd number")


if __name__ == "__main__":
    main()
