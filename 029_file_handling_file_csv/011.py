"""

Write a Python program to write a Python dictionary to a csv file.
After writing the CSV file read the CSV file and display the content.

csv_columns = ['id', 'Column1', 'Column2', 'Column3', 'Column4', 'Column5']

data = [
    {'id': '1', 'Column1': 33, 'Column2': 35, 'Column3': 21, 'Column4': 71, 'Column5': 10},
    {'id': '2', 'Column1': 25, 'Column2': 30, 'Column3': 40, 'Column4': 25, 'Column5': 10},
    {'id': '3', 'Column1': 56, 'Column2': 30, 'Column3': 55, 'Column4': 55, 'Column5': 40}
]

"""

import csv

__out_file_path = "011.csv"


def main():
    csv_columns = ['id', 'Column1', 'Column2', 'Column3', 'Column4', 'Column5']

    data = [
        {'id': '1', 'Column1': 33, 'Column2': 35, 'Column3': 21, 'Column4': 71, 'Column5': 10},
        {'id': '2', 'Column1': 25, 'Column2': 30, 'Column3': 40, 'Column4': 25, 'Column5': 10},
        {'id': '3', 'Column1': 56, 'Column2': 30, 'Column3': 55, 'Column4': 55, 'Column5': 40}
    ]

    with open(__out_file_path, 'w', newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns, quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

    with open(__out_file_path, "r", newline="") as f:
        reader = csv.reader(f, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            print(row)


if __name__ == "__main__":
    main()
