"""

Write a Python program to display formatted text (width=100) as output.


Center: $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Test$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
Left  : Test$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
Right : $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Test


Python is a widely used high-level, general-purpose, interpreted,
dynamic programming language. Its design philosophy emphasizes
code readability, and its syntax allows programmers to express
concepts in fewer lines of code than possible in languages such
as C++ or Java.


Python is a widely used high-level, general-purpose, interpreted, dynamic programming language. Its
design philosophy emphasizes code readability, and its syntax allows programmers to express concepts
in fewer lines of code than possible in languages such as C++ or Java.


"""

import textwrap


def main():
    s = "Test"
    print(f"Center: {s:$^100}")
    print(f"Left  : {s:$<100}")
    print(f"Right : {s:$>100}")

    print()

    s = """Python is a widely used high-level, general-purpose, interpreted,
dynamic programming language. Its design philosophy emphasizes
code readability, and its syntax allows programmers to express
concepts in fewer lines of code than possible in languages such
as C++ or Java."""

    print(textwrap.fill(s, width=100))


if __name__ == "__main__":
    main()
