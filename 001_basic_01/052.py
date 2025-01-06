"""

Write a Python program to print to STDERR.

At program startup, three text streams are predefined and need not be opened explicitly:
    standard input (for reading conventional input),
    standard output (for writing conventional output),
    and standard error (for writing diagnostic output).

As initially opened, the standard error stream is not fully buffered; the standard input and standard output
streams are fully buffered if and only if the stream can be determined not to refer to an interactive device.

The purpose of the standard error stream is to separate error messages from regular output.
"""

# Import the 'print_function' feature from the '__future__' module to enable Python 3-style print function.
# to bring the print function from Python 3 into Python 2.6+
from __future__ import print_function

import sys


def eprint(*args, **kwargs):
    """Redirect the output to the standard error stream - STDERR using the sys module"""
    print(*args, file=sys.stderr, **kwargs)


def main():
    print("Hello World!", "This is a test", sep='\n', end='\n')


if __name__ == "__main__":
    main()
