"""

Write a Python program to find the second lowest total marks of any student(s) from the given names and marks of
each student using lists and lambda. Input the number of students, the names and grades of each student.

Input number of students: 5
Name: S ROY
Grade: 1
Name: B BOSE
Grade: 3
Name: N KAR
Grade: 2
Name: C DUTTA
Grade: 1
Name: G GHOSH
Grade: 1

Names and Grades of all students:
[['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH', 1.0]]

Second lowest grade: 2.0
Names:
N KAR

"""

from heapq import nlargest


def main():
    n = int(input("Enter the number of students: "))
    lst = []

    while len(lst) < n:
        name, grade = input("Enter the name and the grade comma-separated: ").split(",")
        lst.append((name, float(grade)))

    print(lst)
    worst = nlargest(2, lst, key=lambda _: _[1])
    print(worst[-1][0])
    print(worst[-1][1])


if __name__ == "__main__":
    main()
