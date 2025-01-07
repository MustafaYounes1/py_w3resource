"""

Write a Python program to remove spaces from dictionary keys.

student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}

{'S001': ['Math', 'Science'], 'S002': ['Math', 'English']}

"""


def main():
    student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
    print({k.replace(" ", ""): v for k, v in student_list.items()})


if __name__ == "__main__":
    main()
