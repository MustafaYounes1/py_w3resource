"""

Write a Python program that displays your name, age, and address on three different lines.

"""


def main():
    info = input("Enter your name, age, and address (comma-separated): ").split("-")
    for _ in info:
        print(_.strip())


if __name__ == "__main__":
    main()
