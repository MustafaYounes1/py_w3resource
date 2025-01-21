"""

Write a Python program that executes an operation on a list and handles an IndexError exception if the index is
out of range.

"""


def main():
    try:
        lst = [1, 2]
        print(lst[2])

    except IndexError as e:
        print(e)


if __name__ == "__main__":
    main()
