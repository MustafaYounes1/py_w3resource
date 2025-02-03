"""

Write a Python program to convert a Unix timestamp string to a readable date.

Sample Unix timestamp string:  1284105682
Expected Output:               2010-09-10 11:01:22

"""

from datetime import datetime


def main():
    ts = 1284105682
    print(datetime.fromtimestamp(ts))


if __name__ == "__main__":
    main()
