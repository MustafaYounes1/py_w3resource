"""

Write a Python program to create a csv that contain the following data:

id1,id2,date
1,a,01/01/2019
2,b,01/02/2019
3,c,01/03/2019

"""

import csv

__out_file_path = "009.csv"


def main():
    with open(__out_file_path, "w", newline="") as f:
        csv_writer = csv.writer(f, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)

        csv_writer.writerow(("id1", "id2", "date"))

        csv_writer.writerow((1, "a", "01/01/2019"))
        csv_writer.writerow((2, "b", "01/02/2019"))
        csv_writer.writerow((3, "c", "01/03/2019"))


if __name__ == "__main__":
    main()
