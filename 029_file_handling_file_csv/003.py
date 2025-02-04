"""

Write a Python program to read a given CSV file as a list.
    Input file: 003.csv

[
    ['employ_id', 'first_name', 'last_name', 'email', 'phone_number', 'hire_date', 'job_id', 'salary',
    'commission_pct', 'manager_id', 'department_id'],
    ['100', 'Steven', 'King', 'SKING', '515.123.4567', '1987-06-17', 'AD_PRES', '24000', '', '', '90'],
    ['101', 'Neena', 'Kochhar', 'NKOCHHAR', '515.123.4568', '1987-06-18', 'AD_VP', '17000', '', '100', '90'],
    ['102', 'Lex', 'De Haan', 'LDEHAAN', '515.123.4569', '1987-06-19', 'AD_VP', '17000', '', '100', '90']
]
"""

import csv

__in_file_path = "003.csv"


def main():
    with open(__in_file_path, "r", newline="") as f:
        csv_reader = csv.reader(f, delimiter=",")
        print(list(csv_reader))


if __name__ == "__main__":
    main()
