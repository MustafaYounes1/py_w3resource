"""

Write a Python program to get system time.

"""

from datetime import datetime


def main():
    print(datetime.now().strftime("%I:%M:%S %p"))


if __name__ == "__main__":
    main()
