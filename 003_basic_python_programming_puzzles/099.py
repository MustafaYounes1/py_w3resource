"""

Write a Python program to find a string such that, when three or more spaces are compacted to a '-' and one or two
spaces are replaced by underscores, leads to the target.

Python-Exercises                        =>  Python   Exercises
Python_Exercises                        =>  Python Exercises
-Hello,_world!__This_is-so-easy!-       =>  Hello, world!  This is   so   easy!

"""


__data = [
    "Python-Exercises",
    "Python_Exercises",
    "-Hello,_world!__This_is-so-easy!-"
]


def main():
    for w in __data:
        w = w.replace("-", "   ").replace("_", "  ").strip()
        print(w)


if __name__ == "__main__":
    main()
