"""

126. Write a Python program to get the actual module object for a given object.

e.g. inspect that the `sqrt` function is implemented in the builtin `math` module

Hint: use the `inspect` builtin module

"""

# The inspect module provides several useful functions to help get information about live objects such as modules,
# classes, methods, functions, tracebacks, frame objects, and code objects.
import inspect
from math import sqrt


def main():
    # Return the name of the module named by the file path, without including the names of enclosing packages.
    print(inspect.getmodule(sqrt))


if __name__ == "__main__":
    main()
