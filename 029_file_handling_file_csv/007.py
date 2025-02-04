"""

Write a Python program to read specific columns of a given CSV file and print the content of the columns.
    Input file: 001.csv
    Get: department_id, department_name

10 Administration
20 Marketing
30 Purchasing
40 Human Resources
50 Shipping
60 IT
70 Public Relations
80 Sales
90 Executive
100 Finance
110 Accounting
120 Treasury
130 Corporate Tax
140 Control And Credit
150 Shareholder Services
160 Benefits
170 Manufacturing
180 Construction
190 Contracting
200 Operations
210 IT Support
220 NOC
230 IT Helpdesk
240 Government Sales
250 Retail Sales
260 Recruiting
270 Payroll

"""

import csv

__in_file_path = "001.csv"


def main():
    with open(__in_file_path, "r", newline="") as f:
        csv_reader = csv.DictReader(f, delimiter=",")
        for r in csv_reader:
            print(r["department_id"], r["department_name"])


if __name__ == "__main__":
    main()
