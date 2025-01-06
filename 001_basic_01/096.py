"""

Write a Python program to print the current call stack.

Hint: Use the 'traceback' module

"""

# This module provides a standard interface to extract, format and print stack traces of Python programs.
import traceback


def f1():
    print("Deepest call")
    print("f1 calling stack: ")
    traceback.print_stack()


def f2():
    print("f2 calling f1")
    f1()


def f3():
    print("f3 calling f2")
    f2()


def main():
    f3()


if __name__ == "__main__":
    main()
