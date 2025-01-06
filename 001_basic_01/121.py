"""

Write a Python program to determine if a variable is defined or not.

"""


def main():
    try:
        print(x)
    except NameError as err:
        print(f"Error occurred: {err}")


if __name__ == "__main__":
    main()
