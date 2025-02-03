"""

Write a Python program to parse a string representing time and return the time structure.

22 January, 2020

time.struct_time(tm_year=2020, tm_mon=1, tm_mday=22, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=2, tm_yday=22, tm_isdst=-1)

"""

import time


def main():
    s = "22 January, 2020"
    print(time.strptime(s, "%d %B, %Y"))


if __name__ == "__main__":
    main()
