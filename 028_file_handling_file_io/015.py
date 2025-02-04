"""

Write a Python program to assess if a file is closed or not.
    Input file: 001.txt

Inside the open context manager: False
Outside the open context manager: True

"""

__in_file_path = "001.txt"


def main():
    with open(__in_file_path) as f:
        print(f"Inside the open context manager: {f.closed}")

    print(f"Outside the open context manager: {f.closed}")


if __name__ == "__main__":
    main()
