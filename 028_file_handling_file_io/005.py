"""

Write a Python program to read a file and store its into a list.
    Input file: 001.txt

[
    'Welcome to w3resource.com.\n',
    'Append this text.Append this text.Append this text.\n',
    'Append this text.\n',
    'Append this text.\n',
    'Append this text.\n',
    'Append this text.\n'
]

"""

__in_file_path = "001.txt"


def main():
    with open(__in_file_path, "r") as f:
        print(f.readlines())


if __name__ == "__main__":
    main()
