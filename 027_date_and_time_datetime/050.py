"""

Write a Python program to get a list of dates between two dates.

2025-01-25, 2025-02-03

2025-01-26
2025-01-27
2025-01-28
2025-01-29
2025-01-30
2025-01-31
2025-02-01
2025-02-02

"""

from datetime import date, datetime, timedelta
from typing import Generator


def get_dates_between(d1: date, d2: date) -> Generator[date, None, None]:
    assert d1 < d2, "Invalid input"

    id_ = d1 + timedelta(days=1)
    while id_ < d2:
        yield id_
        id_ += timedelta(days=1)


def main():
    s1, s2 = "2025-01-25", "2025-02-03"
    d1, d2 = map(lambda _: datetime.strptime(_, "%Y-%m-%d").date(), (s1, s2))

    gen = get_dates_between(d1, d2)
    for _ in gen:
        print(_)


if __name__ == "__main__":
    main()
