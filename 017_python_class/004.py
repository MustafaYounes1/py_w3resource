"""

'builtins' module provides direct access to all 'built-in' identifiers of Python.

Write a Python program that imports the abs() function using the builtins module, displays the documentation of
the abs() function and finds the absolute value of -155.

Help on built-in function abs in module builtins:

abs(x, /)
    Return the absolute value of the argument.

155

"""

from builtins import abs


def main():
    help(abs)
    # or for fewer details
    # print(abs.__doc__)
    print(abs(-155))


if __name__ == "__main__":
    main()
