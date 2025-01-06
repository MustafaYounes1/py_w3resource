"""

Write a Python program to determine the index of a given string at which a certain substring starts.
If the substring is not found in the given string return 'Not found'.

Python Exercises, Ex
Python Exercises, yt
Python Exercises, PY

"""


def main():
    s1, s2 = input("Enter the two string comma-separated: ").split(", ")
    idx = s1.find(s2)
    print(idx if idx != -1 else "Not found")


if __name__ == "__main__":
    main()
