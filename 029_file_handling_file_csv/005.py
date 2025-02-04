"""

Write a Python program to read a given CSV files with initial spaces after a delimiter and remove those initial spaces.
    Input file: 005.csv

['department_id', 'department_name', 'manager_id', 'location_id']
['10', 'Administration', '200', '1700']
['20', 'Marketing', '201', '1800']

"""

import csv

__in_file_path = "005.csv"


def main():
    with open(__in_file_path, "r", newline="") as f:
        csv_reader = csv.reader(f, delimiter=",", skipinitialspace=True)
        for row in csv_reader:
            print(row)


if __name__ == "__main__":
    main()
