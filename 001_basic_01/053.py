"""

Write a Python program to access environment variables.

Try to print the PATH environment variable

"""

import os


def main():
    # all environment variable
    for _ in os.environ:
        print(_)

    print("=" * 25)

    print(f"PATH Env Var: {os.environ['PATH']}")


if __name__ == "__main__":
    main()
