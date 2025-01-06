"""

Write a Python program to list the special variables used in the language.

"""

import textwrap


def main():
    # globals() Return the dictionary implementing the current module namespace.

    # The __builtins__ module consists of a set of builtin names for the built-ins namespace. Most, if not all,
    # of these names come from the __builtin__ module, which is a module of the built-in functions, exceptions,
    # and other attributes. In standard Python execution, __builtins__ contains all the names from __builtin__ .

    python_vars = set(globals()) | set(__builtins__.__dict__.keys())
    string = " | ".join(python_vars)
    print(textwrap.fill(string, 50))


if __name__ == "__main__":
    main()
