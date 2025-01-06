"""

Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).

Sample function : abs()

Expected Result :
=================
abs(number) -> number
Return the absolute value of the argument.

"""


def main():
    # A docstring is a string literal that occurs as the first statement in a module, function, class, or
    # method definition. Such a docstring becomes the __doc__ special attribute of that object.
    print(abs.__doc__)


if __name__ == "__main__":
    main()
