"""

Write a Python program that accepts the user's first and last name and prints them in reverse order with
a space between them.

"""


def main():
    full_name = input("Enter your fullname: ")
    print(" ".join(full_name.split()[-1::-1]))


if __name__ == "__main__":
    main()
