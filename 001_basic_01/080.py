"""

Write a Python program to get the current value of the recursion limit.

Hint: use 'sys' module

"""

import sys


def main():
    # the recursion limit, the maximum depth of the Python interpreter stack. This limit prevents infinite recursion
    # from causing an overflow of the C stack and crashing Python.
    # The highest possible limit is platform-dependent.
    print(f"Current recursion limit is: {sys.getrecursionlimit()}")

    # Set the maximum depth of the Python interpreter stack to limit
    # A user may need to set the limit higher when they have a program that requires deep recursion and a platform
    # that supports a higher limit. This should be done with care, because a too-high limit can lead to a crash.
    # sys.setrecursionlimit(limit)


if __name__ == "__main__":
    main()
