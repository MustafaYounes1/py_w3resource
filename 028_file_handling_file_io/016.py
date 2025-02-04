"""

Write a Python program to remove newline characters from a file.
    Input file: 001.txt

['Welcome to w3resource.com.', 'Append this text.Append this text.Append this text.', 'Append this text.',
'Append this text.', 'Append this text.', 'Append this text.']

"""

__in_file_path = "001.txt"


def main():
    with open(__in_file_path, "r") as f:
        lines = f.read().splitlines(keepends=False)
        print(lines)


if __name__ == "__main__":
    main()
