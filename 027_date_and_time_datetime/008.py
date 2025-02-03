"""

Write a Python program to convert the date to datetime (midnight of the date) in Python.
Sample Output : 2025-02-02 00:00:00

"""

from datetime import datetime


def main():
    d = datetime.combine(datetime.now().date(), datetime.min.time())
    print(d)


if __name__ == "__main__":
    main()
