"""

Write a Python program that implements a Python program that filters out dates (in the format "YYYY-MM-DD") that are
in the future using the filter function.

Note: the date at the time of writing of this doc: 2025-01-28

["2023-07-11", "2022-02-22", "2024-05-11", "3040-12-31", "2021-01-01"]      =>  ['3040-12-31']

"""

from datetime import datetime


def main():
    lst = ["2023-07-11", "2022-02-22", "2024-05-11", "3040-12-31", "2021-01-01"]
    print(list(filter(lambda _: datetime.strptime(_, "%Y-%m-%d").date() > datetime.now().date(), lst)))


if __name__ == "__main__":
    main()
