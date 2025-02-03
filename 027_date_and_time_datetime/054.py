"""

The epoch is the point where time starts, and is platform dependent. For Unix, the epoch is January 1, 1970,
00:00:00 (UTC). Write a Python program to find out what the epoch is on a given platform. Convert a given time in
seconds since the epoch (3600).

1970-01-01 00:00:00
1970-01-01 01:00:00

"""

import time


def main():
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(0)))
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(3600)))


if __name__ == "__main__":
    main()
