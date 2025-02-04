"""

Write a Python program to read a given CSV file having tab delimiter.
    Input file: 002.csv

['country_id', 'country_name', 'region_id']
['AR', 'Argentina', '2']
['AU', 'Australia', '3']

"""

import csv

__in_file_path = "002.csv"


def main():
    with open(__in_file_path, "r", newline="") as f:
        csv_reader = csv.reader(f, delimiter="\t")
        for line in csv_reader:
            print(line)


if __name__ == "__main__":
    main()
