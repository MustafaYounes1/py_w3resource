"""

Write a Python program to insert space before every capital letter appears in a given word.

PythonExercises                         -> "Python Exercises"
Python                                  -> "Python"
PythonExercisesPracticeSolution         -> "Python Exercises Practice Solution"

"""


def main():
    s = input("Enter a string: ")
    print("".join([s[0]] + [f' {_}' if _.isupper() else _ for _ in s[1:]]))


if __name__ == "__main__":
    main()
