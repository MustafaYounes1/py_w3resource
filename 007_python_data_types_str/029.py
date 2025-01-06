"""

Write a Python program to set the indentation of the first line.

"""

import textwrap


def main():
    s = """Python is a widely used high-level, general-purpose, interpreted, dynamic
programming language. Its design philosophy emphasizes code readability,
and its syntax allows programmers to express concepts in fewer lines of
code than possible in languages such as C++ or Java."""

    print(textwrap.fill(s, initial_indent="    ", width=80))


if __name__ == "__main__":
    main()
