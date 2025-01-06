"""

Write a Python program that retrieves the date and time of file creation and modification.

"""

from datetime import datetime
import pathlib


def main():
    file_path = pathlib.Path(input("Enter the file path: "))
    assert file_path.is_file(), f"{file_path} doesn't exist"
    print(f"Created in: {datetime.fromtimestamp(file_path.stat().st_ctime).strftime('%Y-%m-%d %I:%M:%S %p')}")
    print(f"Updated in: {datetime.fromtimestamp(file_path.stat().st_mtime).strftime('%Y-%m-%d %I:%M:%S %p')}")


if __name__ == "__main__":
    main()
