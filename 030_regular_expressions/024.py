"""

Write a Python program to extract year, month and date (yyyy/mm/dd) from a URL.

"https://www.washingtonpost.com/news/football-insider/wp/2016/12/2/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"

year: 2016, month: 12, day: 2

"""

import re


def main():
    url = "https://www.washingtonpost.com/news/football-insider/wp/2016/12/2/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
    ma = re.search(r"""
        (?P<year>\d{4})             # YEAR
        /(?P<month>\d{1,2})         # Month
        /(?P<day>\d{1,2})           # DAY
    """,
        url,
        re.VERBOSE
    )
    if ma:
        print(f"year: {ma.group('year')}, month: {ma.group('month')}, day: {ma.group('day')}")
    else:
        print("Failed to fetch the date from the URL")


if __name__ == "__main__":
    main()
