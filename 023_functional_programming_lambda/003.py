"""

Write a Python program to sort a list of tuples using Lambda.

[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

"""


def main():
    lst = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
    print(sorted(lst, key=lambda _: _[1]))


if __name__ == "__main__":
    main()
