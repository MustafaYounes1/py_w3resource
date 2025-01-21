"""

Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

"""


def main():
    try:
        res = 2 / 0
        print(res)

    except ZeroDivisionError as e:
        print(e)


if __name__ == "__main__":
    main()
