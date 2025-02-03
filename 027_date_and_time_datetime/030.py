"""

Write a Python program to convert the current date and time to a timestamp.

>   1738590568.194068

"""

from datetime import datetime


def main():
    print(datetime.now().timestamp())


if __name__ == "__main__":
    main()
