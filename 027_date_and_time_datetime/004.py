"""

Write a Python program to get the current time in Python.
Sample Format :  18:43:06.408675

"""

from datetime import datetime


def main():
    print(datetime.now().time())


if __name__ == "__main__":
    main()
