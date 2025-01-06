"""

Write a Python program to add prefix text to all of the lines in a string.

"""


def main():
    s = """    Python is a widely used high-level, general-purpose, interpreted,
dynamic programming language. Its design philosophy emphasizes
code readability, and its syntax allows programmers to express
concepts in fewer lines of code than possible in languages such
as C++ or Java."""

    pfx = '> '

    print("\n".join([pfx + _ for _ in s.split("\n")]))


if __name__ == "__main__":
    main()
