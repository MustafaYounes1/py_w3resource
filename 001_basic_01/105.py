"""

Write a Python program to get the environment variables and print them in a neat way.

"""

import os
# provides a capability to “pretty-print” arbitrary Python data structures in a form which can be used as input to
# the interpreter
import pprint


def main():
    pprint.pprint(dict(os.environ), width=150)


if __name__ == "__main__":
    main()
