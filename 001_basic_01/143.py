"""

Write a Python program to determine if the Python shell is executing in 32-bit or 64-bit mode on the operating system.

"""

import platform


def main():
    print(f"Python shell is executing in {platform.architecture()[0]} mode")


if __name__ == "__main__":
    main()
