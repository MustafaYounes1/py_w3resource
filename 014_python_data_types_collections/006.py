"""

Write a Python program that accepts the number of subjects, subject names and marks. Input the number of subjects and
then the subject name and marks separated by a space on the next line. Print the subject name and marks in order of
appearance.

Note: try to use the OrderedDict

Number of subjects: 3
Input Subject name and marks: Bengali 58
Input Subject name and marks: English 62
Input Subject name and marks: Math 68
Bengali 58
English 62
Math 6

"""

from collections import OrderedDict


def main():
    data = OrderedDict()
    n = int(input("Enter the number of subjects: "))

    for _ in range(n):
        k, v = input("Enter the subject name and the grade white-separated: ").split()
        data[k] = v

    for k in data:
        print(k, data[k])


if __name__ == "__main__":
    main()
