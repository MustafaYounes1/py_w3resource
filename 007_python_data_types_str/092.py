"""

Write a Python program to find string similarity between two given strings.

Hint: use the difflib SequenceMatcher

Python Exercises, Python Exercises    =>  1.0
Python Exercises, Python Exercise     =>  0.967741935483871
Python Exercises, Python Ex.          =>  0.6923076923076923
Python Exercises, Python              =>  0.5454545454545454
Java Exercises, Python                =>  0.0

"""

from difflib import SequenceMatcher


def main():
    s1, s2 = input("Enter two comma-separated strings: ").split(", ")
    matcher = SequenceMatcher(None, s1, s2)
    print(matcher.ratio())


if __name__ == "__main__":
    main()
