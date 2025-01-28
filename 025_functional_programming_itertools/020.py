"""

Write a Python program to find the years between 2000 and 2150 when the 25th of December is a Sunday.

[2005, 2011, 2016, 2022, 2033, 2039, 2044, 2050, 2061, 2067, 2072, 2078, 2089, 2095, 2101, 2107, 2112, 2118, 2129,
2135, 2140, 2146]

"""

from datetime import date
from itertools import count, islice


def main():
    print(list(filter(lambda y: date(year=y, month=12, day=25).weekday() == 6, islice(count(2000), 151))))


if __name__ == "__main__":
    main()
