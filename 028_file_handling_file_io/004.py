"""

Write a Python program to read last n lines of a file.
    Input file: 001.txt
    Read the last two lines

Append this text.
Append this text.

"""

__in_file_path = "001.txt"


def main():
    with open(__in_file_path, "r") as f:
        lines = f.readlines()
        print("".join(lines[-2:]), end='')


if __name__ == "__main__":
    main()
