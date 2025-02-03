"""

Write a Python program to convert a given time in seconds since the epoch to a string representing local time.

236543789   =>  Thu Jun 30 21:36:29 1977

"""

import time


def main():
    print(time.ctime(236543789))


if __name__ == "__main__":
    main()
