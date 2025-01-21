"""

Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.

"""


def main():
    try:
        res = 4 / 0
        print(res)

    # The base class for those built-in exceptions that are raised for various arithmetic errors: OverflowError,
    # ZeroDivisionError, FloatingPointError.
    except ArithmeticError as e:
        print(e)


if __name__ == "__main__":
    main()
