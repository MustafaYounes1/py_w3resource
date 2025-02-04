"""

Write a Python program to count the number of lines in a text file.
    Input file: 007.txt

6

"""

__in_file_path = "007.txt"


def main():
    with open(__in_file_path, "r") as f:
        print(len(f.readlines()))


if __name__ == "__main__":
    main()
