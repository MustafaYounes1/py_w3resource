"""

Write a Python program to write a Python list of lists to a csv file.
After writing the CSV file read the CSV file and display the content.

[[10,'a1', 1], [12,'a2', 3], [14, 'a3', 5], [16, 'a4', 7], [18, 'a5', 9]]

"""

import csv

__out_file_path = "010.csv"


def main():
    data = [[10,'a1', 1], [12,'a2', 3], [14, 'a3', 5], [16, 'a4', 7], [18, 'a5', 9]]

    with open(__out_file_path, "w", newline="") as f:
        csv_writer = csv.writer(f, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writerows(data)

    with open(__out_file_path, "r", newline="") as f:
        csv_reader = csv.reader(f, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
        for r in csv_reader:
            print(r)


if __name__ == "__main__":
    main()
