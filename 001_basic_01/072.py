"""

Write a Python program to get the details of the math module.

"""

import math


def main():
    # using the 'dir' builtin function
    # Without arguments, return the list of names in the current local scope. With an argument, attempt to return a
    # list of valid attributes for that object.
    print(dir(math))

    print("-" * 25)

    # using the 'help' builtin function
    # Invoke the built-in help system. (This function is intended for interactive use.) If no argument is given,
    # the interactive help system starts on the interpreter console. If the argument is a string, then the string
    # is looked up as the name of a module, function, class, method, keyword, or documentation topic, and a help page
    # is printed on the console. If the argument is any other kind of object, a help page on the object is generated.
    help(math)


if __name__ == "__main__":
    main()
