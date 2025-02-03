"""

Write a Python program to create 12 fixed dates from a specified date over a given period.
The difference between two dates is 20.

Current date: 2025-02-03

2025-02-23
2025-03-15
2025-04-04
2025-04-24
2025-05-14
2025-06-03
2025-06-23
2025-07-13
2025-08-02
2025-08-22
2025-09-11
2025-10-01

"""

from datetime import date, timedelta
from itertools import islice
from typing import Generator


def after_20_days(d: date) -> Generator[date, None, None]:
    id_ = d + timedelta(days=20)
    yield id_

    while True:
        id_ += timedelta(days=20)
        yield id_


def main():
    d = date.today()
    print(f"Current date: {d}")

    gen = after_20_days(d)
    for _ in islice(gen, 12):
        print(_)


if __name__ == "__main__":
    main()
