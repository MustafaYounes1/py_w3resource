"""

Write a Python program to read each row from a given csv file and print it.
    Input file: 001.csv

department_id | department_name | manager_id | location_id
10 | Administration | 200 | 1700
20 | Marketing | 201 | 1800
30 | Purchasing | 114 | 1700
40 | Human Resources | 203 | 2400
50 | Shipping | 121 | 1500
60 | IT | 103 | 1400
70 | Public Relations | 204 | 2700
80 | Sales | 145 | 2500
90 | Executive | 100 | 1700
100 | Finance | 108 | 1700
110 | Accounting | 205 | 1700
120 | Treasury |  | 1700
130 | Corporate Tax |  | 1700
140 | Control And Credit |  | 1700
150 | Shareholder Services |  | 1700
160 | Benefits |  | 1700
170 | Manufacturing |  | 1700
180 | Construction |  | 1700
190 | Contracting |  | 1700
200 | Operations |  | 1700
210 | IT Support |  | 1700
220 | NOC |  | 1700
230 | IT Helpdesk |  | 1700
240 | Government Sales |  | 1700
250 | Retail Sales |  | 1700
260 | Recruiting |  | 1700
270 | Payroll |  | 1700

"""

import csv

__in_file_path = "001.csv"


def main():
    with open(__in_file_path, "r", newline="") as f:
        csv_reader = csv.reader(f, delimiter=",")
        for line in csv_reader:
            print(" | ".join(line))


if __name__ == "__main__":
    main()
