"""

Write a Python program that takes a given number of seconds and passes since the epoch as an argument.
Print structure time in local time.

414538698
time.struct_time(tm_year=1983, tm_mon=2, tm_mday=20, tm_hour=0, tm_min=38, tm_sec=18, tm_wday=6, tm_yday=51, tm_isdst=0)

"""

import time


def main():
    print(time.localtime(414538698))


if __name__ == "__main__":
    main()
