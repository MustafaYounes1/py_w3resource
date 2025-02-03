"""

Write a Python program to find the date of the first Monday of a given week.

Sample Year and week:       2015, 50
Expected Output:            Mon Dec 14 2015

"""

from datetime import datetime


def main():
    print(datetime.strptime("2015, 50, 1", "%Y, %W, %w").strftime("%a %b %d %Y"))


if __name__ == "__main__":
    main()
