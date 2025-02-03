"""

Write a Python program to convert a string to datetime.

Sample String : Jul 1 2014 2:43PM
Expected Output : 2014-07-01 14:43:00

"""

from datetime import datetime


def main():
    str_d = "Jul 1 2014 2:43PM"
    print(datetime.strptime(str_d, "%b %d %Y %I:%M%p"))


if __name__ == "__main__":
    main()
