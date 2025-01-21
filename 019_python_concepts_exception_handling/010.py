"""

Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does
not exist.

"""


def main():
    try:
        lst = [1, 2]
        print(lst.rotate())

    except AttributeError as e:
        print(e)


if __name__ == "__main__":
    main()
