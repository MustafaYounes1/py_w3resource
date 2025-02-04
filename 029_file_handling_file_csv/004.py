"""

Write a Python program to read a given CSV file as a dictionary.
    Input file: 004.csv

"""

import csv

__in_file_path = "004.csv"


def main():
    with open(__in_file_path, "r", newline="") as f:
        csv_reader = csv.DictReader(f, delimiter=",")
        for row in csv_reader:
            print(dict(row))


if __name__ == "__main__":
    main()
