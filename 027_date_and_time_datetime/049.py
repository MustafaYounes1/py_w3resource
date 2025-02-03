"""

Write a Python program to convert a string into datetime

2025/02/03  08:11:47 pm     =>  2025-02-03 20:11:47

"""

from datetime import datetime


def main():
    s = "2025/02/03  08:11:47 pm"
    print(datetime.strptime(s, "%Y/%m/%d %I:%M:%S %p"))


if __name__ == "__main__":
    main()
