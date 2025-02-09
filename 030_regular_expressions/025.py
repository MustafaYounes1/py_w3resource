"""

Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

"2025-02-09; 1996-11-01; 2024-09-26"      =>  09-02-2025; 01-11-1996; 26-09-2024

"""

import re


def main():
    s = "2025-02-09; 1996-11-01; 2024-09-26"

    ns = re.sub(
        r"""
        (?P<year>\d{4})-        # YEAR
        (?P<month>\d{1,2})-     # MONTH
        (?P<day>\d{1,2})        # DAY
        """,
        r"\g<day>-\g<month>-\g<year>",
        s,
        flags=re.VERBOSE
    )

    print(ns)


if __name__ == "__main__":
    main()
