"""

Write a Python program that sums the length of a list of names after removing those that start with lowercase letters.
Use the lambda function.

['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']   =>  16

"""


def main():
    lst = ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']
    print(sum(map(lambda _: len(_) if _ and (_[0].isupper()) else 0, lst)))


if __name__ == "__main__":
    main()
