"""

Write a Python program to convert a string date to a timestamp.

01/10/2016  =>  1475269200.0

"""

from datetime import datetime


def main():
    s = "01/10/2016"
    print(datetime.strptime(s, "%d/%m/%Y").timestamp())


if __name__ == "__main__":
    main()
