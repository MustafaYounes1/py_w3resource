"""

Write a Python program to find the available built-in modules.

Hint: use the 'sys' module

"""

import sys

# For text wrapping
import textwrap


def main():
    # A tuple of strings containing the names of all modules that are compiled into this Python interpreter.
    modules = sys.builtin_module_names

    modules_as_str = ','.join(modules).strip()

    # Wraps the single paragraph in text, and returns a single string containing the wrapped paragraph
    wrapped_str = textwrap.fill(modules_as_str, 50)

    print(wrapped_str)


if __name__ == "__main__":
    main()
