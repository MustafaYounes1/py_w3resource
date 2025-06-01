"""

Write a Python program that defines a NamedTuple called Employee with fields like name, age, and country.
Print each employee's name and country.

Klaes Susana, 35, USA
Auxentius Cloe, 44, Canada
Golzar Merob, 28, UK
Tatjana Adhelm, 30, Australia

->
    Klaes Susana    is from USA
    Auxentius Cloe  is from Canada
    Golzar Merob    is from UK
    Tatjana Adhelm  is from Australia

"""

from collections import namedtuple


def main():
   data = [
       ["Klaes Susana", 35, "USA"],
       ["Auxentius Cloe", 44, "Canada"],
       ["Golzar Merob", 28, "UK"],
       ["Tatjana Adhelm", 30, "Australia"],
   ]

   employee = namedtuple("Employee", ["full_name", "age", "country"])
   employees = [employee(*emp_data) for emp_data in data]

   for emp in employees:
       print(f"{emp.full_name:15s} is from {emp.country:15s}")


if __name__ == "__main__":
    main()
