"""

Write a Python program to convert GPAs to letter grades according to the following table:

GPAs	Grades
4.0 	A+
3.7 	A
3.4 	A-
3.0 	B+
2.7 	B
2.4 	B-
2.0 	C+
1.7 	C
1.4 	C-
below   F

Input:
[4.0, 3.5, 3.8]
Output:
['A+', 'A-', 'A']

Input:
[5.0, 4.7, 3.4, 3.0, 2.7, 2.4, 2.0, 1.7, 1.4, 0.0]
Output:
['A+', 'A+', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'F']

"""


def grades(g):
    if g >= 4.0:
        return "A+"

    elif 3.7 <= g < 4.0:
        return "A"

    elif 3.4 <= g < 3.7:
        return "A-"

    elif 3.0 <= g < 3.4:
        return "B+"

    elif 2.7 <= g < 3.0:
        return "B"

    elif 2.4 <= g < 2.7:
        return "B-"

    elif 2.0 <= g < 2.4:
        return "C+"

    elif 1.7 <= g < 2.0:
        return "C"

    elif 1.4 <= g < 1.7:
        return "C-"

    else:
        return "F"


def main():
    seq = list(map(float, input("Enter a list of comma-separated numbers: ").split(",")))
    print(
        [grades(_) for _ in seq]
    )


if __name__ == "__main__":
    main()
