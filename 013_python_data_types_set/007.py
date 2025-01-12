"""

Write a Python program to create a union of sets.

{'blue', 'green'}
{'blue', 'yellow'}

{'blue', 'yellow', 'green'}

"""


def main():
    s1 = {'blue', 'green'}
    s2 = {'blue', 'yellow'}
    print(s1 | s2)


if __name__ == "__main__":
    main()
