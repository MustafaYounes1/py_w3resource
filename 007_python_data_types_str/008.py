"""

Write a Python function that takes a list of words and return the longest word and the length of the longest one.

["PHP", "Exercises", "Backend"]

Longest word: Exercises
Length of the longest word: 9

"""


def main():
    lst = ["PHP", "Exercises", "Backend"]
    m = max(lst, key=len)
    print(m, len(m))


if __name__ == "__main__":
    main()
