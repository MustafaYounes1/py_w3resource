"""

Write a Python program to read a file line by line and store its first 3 lines into a list.
    Input file: 001.txt

['Welcome to w3resource.com.\n', 'Append this text.Append this text.Append this text.\n', 'Append this text.\n']

"""

from itertools import islice

__in_file_path = "001.txt"


def main():
    f = open(__in_file_path, "r")
    print(list(islice(f, 3)))
    f.close()


if __name__ == "__main__":
    main()
