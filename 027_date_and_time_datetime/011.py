"""

Write a Python program to convert Year/Month/Day to Day of Year in Python.

2025/02/02  =>  033

"""

from datetime import datetime


def main():
    str_d = "2025/02/02"
    print(datetime.strptime(str_d, "%Y/%m/%d").strftime("%j"))


if __name__ == "__main__":
    main()
