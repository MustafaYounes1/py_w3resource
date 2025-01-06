"""

Write a Python program to remove duplicate words from a given string.

Python Exercises Practice Solution Exercises

Python Exercises Practice Solution

"""


def main():
    s = input("Enter the sentence: ")
    seen = set()
    out = ""

    for _ in s.split():
        if _ not in seen:
            out += _ + " "
            seen.add(_)

    print(out)


if __name__ == "__main__":
    main()
