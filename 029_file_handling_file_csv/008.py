"""

Write a Python program that prints the number of rows (skipping the header of the file) and the field names.
    Input file: 001.csv

Header: ['department_id', 'department_name', 'manager_id', 'location_id']
#Rows:  27

"""

import csv

__in_file_path = "001.csv"


def main():
    with open(__in_file_path, "r", newline="") as f:
        csv_reader = csv.DictReader(f, delimiter=",")
        print(f"Header: {csv_reader.fieldnames}")
        print(f"#Rows:  {len(list(csv_reader))}")


if __name__ == "__main__":
    main()
