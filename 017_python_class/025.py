"""

Write a Python class Employee with private attributes like emp_id, emp_name, emp_salary, and emp_department and
methods like update_emp_salary, and print_employee_details.

Sample Employee Data:
"ADAMS", "E7876", 50000, "ACCOUNTING"
"JONES", "E7499", 45000, "RESEARCH"
"MARTIN", "E7900", 50000, "SALES"
"SMITH", "E7698", 55000, "OPERATIONS"

Define a setter to change the department of an employee.
Use 'print_employee_details' method to print the details of an employee.
Use 'update_emp_salary' method to update the salary of an employee takes one arguments: the hours_worked, which is
the number of hours worked by the employee. If the number of hours worked is more than 50, the method computes overtime
and adds it to the salary.

Overtime is calculated as following formula:
overtime = hours_worked - 50
Overtime amount = (overtime * (salary / 50))

=====
ToDo:
=====

1. Create the following employees:
    "ADAMS", "E7876", 50000, "ACCOUNTING"
    "JONES", "E7499", 45000, "RESEARCH"
    "MARTIN", "E7900", 50000, "SALES"
    "SMITH", "E7698", 55000, "OPERATIONS"

2. Show the details of each employee

3. Change the departments of some employees:
    the first employee to "OPERATIONS"
    the froth employee to "SALES"

4. Update the salary of some employees based on provided working hours
    the second employee, given his working hours as 52 hours
    the forth employee, given his working hours as 60 hours

5. Show the details of each employee

==================================================
ID: ADAMS
Name: E7876
Salary: 50000
Department: ACCOUNTING
==================================================
ID: JONES
Name: E7499
Salary: 45000
Department: RESEARCH
==================================================
ID: MARTIN
Name: E7900
Salary: 50000
Department: SALES
==================================================
ID: SMITH
Name: E7698
Salary: 55000
Department: OPERATIONS
==================================================
Updating the salary of the second and forth employees based on the working hours:
==================================================
ID: ADAMS
Name: E7876
Salary: 50000
Department: OPERATIONS
==================================================
ID: JONES
Name: E7499
Salary: 46800.0
Department: RESEARCH
==================================================
ID: MARTIN
Name: E7900
Salary: 50000
Department: SALES
==================================================
ID: SMITH
Name: E7698
Salary: 66000.0
Department: SALES
=================================================

"""

from typing import List


class Employee:
    def __init__(self, e_id: str, e_name: str, e_sal: float, e_dep: str):
        self.__e_id: str = e_id
        self.__e_name: str = e_name
        self.__e_sal: float = e_sal
        self.__e_dep: str = e_dep

    @property
    def department(self) -> str:
        return self.__e_dep

    @department.setter
    def department(self, e_dep: str) -> None:
        self.__e_dep = e_dep

    def print_emp_details(self) -> None:
        print(f"ID: {self.__e_id}\nName: {self.__e_name}\nSalary: {self.__e_sal}\nDepartment: {self.__e_dep}")

    def calc_emp_salary(self, hours: float) -> None:
        self.__e_sal = max((hours - 50), 0) * self.__e_sal / 50 + self.__e_sal


def show_employees_details(emp_lst: List[Employee]) -> None:
    print('=' * 50)
    for _ in emp_lst:
        _.print_emp_details()
        print('=' * 50)


def main():
    emp1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
    emp2 = Employee("JONES", "E7499", 45000, "RESEARCH")
    emp3 = Employee("MARTIN", "E7900", 50000, "SALES")
    emp4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")

    show_employees_details([emp1, emp2, emp3, emp4])

    emp1.department = "OPERATIONS"
    emp4.department = "SALES"

    print("Updating the salary of the second and forth employees based on the working hours: ")
    emp2.calc_emp_salary(52)
    emp4.calc_emp_salary(60)

    show_employees_details([emp1, emp2, emp3, emp4])


if __name__ == "__main__":
    main()
