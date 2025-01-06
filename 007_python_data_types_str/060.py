"""

Write a Python program to capitalize the first and last letters of each word in a given string.

python exercises practice solution  =>  PythoN ExerciseS PracticE SolutioN

"""


def main():
    s = "python exercises practice solution"
    print(" ".join([_[0].upper() + _[1:-1] + _[-1].upper() for _ in s.split()]))


if __name__ == "__main__":
    main()
