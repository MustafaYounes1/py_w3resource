"""

Write a Python program to drop microseconds from datetime.

2025-02-02 20:47:11.804563 -> 2025-02-02 20:47:11

"""

from datetime import datetime, timedelta


def main():
    curr_dt = datetime.now()
    print(f"{curr_dt} -> {curr_dt.replace(microsecond=0)}")


if __name__ == "__main__":
    main()
