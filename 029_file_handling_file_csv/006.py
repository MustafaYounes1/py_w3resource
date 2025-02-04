"""

Write a Python program that reads a CSV file and remove initial spaces, quotes around each entry and the delimiter.
    Input file: 006.csv
    Note: try to define a dialect and register it to the csv Module

['country_id', 'country_name', 'region_id']
['AR', 'Argentina', 2.0]
['AU', 'Australia', 3.0]
['BE', 'Belgium', 1.0]
['BR', 'Brazil', 2.0]
['CA', 'Canada', 2.0]

"""

import csv

__in_file_path = "006.csv"


csv.register_dialect(
    "dialect006",
    delimiter="|",
    skipinitialspace=True,
    quoting=csv.QUOTE_NONNUMERIC,
    quotechar='"'
)


def main():
    with open(__in_file_path, "r", newline="") as f:
        csv_reader = csv.reader(f, dialect="dialect006")
        for row in csv_reader:
            print(row)


if __name__ == "__main__":
    main()
