"""

Write a Python program to get the current UTC datetime and convert it to the current timezone and then print it in the
ISO 8601 format

2025-02-03T20:24:31.522622+03:00

"""

from datetime import datetime, timezone


def main():
    local = datetime.now(timezone.utc).astimezone()
    print(local.isoformat())


if __name__ == "__main__":
    main()
