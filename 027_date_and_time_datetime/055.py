"""

Write a Python program to get time values with components using local time and gmtime.

time.struct_time(tm_year=2025, tm_mon=2, tm_mday=3, tm_hour=20, tm_min=44, tm_sec=52, tm_wday=0, tm_yday=34, tm_isdst=0)

"""

import time


def main():
    print(time.localtime())


if __name__ == "__main__":
    main()
