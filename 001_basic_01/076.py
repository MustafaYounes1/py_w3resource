"""

 Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments)
 passed to a script.

 Hint: Use the 'sys' module

"""

import sys


def main():
    # sys.argv The list of command line arguments passed to a Python script
    print(f"File path: {sys.argv[0]}")
    print(f"Number of arguments: {len(sys.argv) - 1}")
    for idx, arg in enumerate(sys.argv[1:]):
        print(f"Arg {idx + 1}: {arg}")


if __name__ == "__main__":
    main()
