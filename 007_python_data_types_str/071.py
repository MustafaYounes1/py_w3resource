"""

Write a Python program to move all spaces to the front of a given string in a single traversal.

Python Exercises    =>  " PythonExercises"

"""


def main():
    s = input("Enter a string: ")
    out = ""

    for _ in s:
        if _ != " ":
            out += _
        else:
            out = " " + out

    print(out)


if __name__ == "__main__":
    main()
