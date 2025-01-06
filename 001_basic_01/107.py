"""

Write a Python program to retrieve file properties.
    File name
    File format
    Most recent access time
    Modified time
    Creating time (ctime)
    Size

"""

from datetime import datetime
import pathlib


def main():
    file_path = pathlib.Path(input("Enter the path: "))
    assert file_path.is_file(), f"{file_path} is not a file"
    strf = "%Y-%m-%d %I:%M:%S %p"
    print(f"File name:                  {file_path.stem}")
    print(f"File format:                {file_path.suffix}")
    print(f"Most recent access time:    {datetime.fromtimestamp(file_path.stat().st_atime).strftime(strf)}")
    print(f"Modified time:              {datetime.fromtimestamp(file_path.stat().st_mtime).strftime(strf)}")
    print(f"Creation time:              {datetime.fromtimestamp(file_path.stat().st_ctime).strftime(strf)}")
    print(f"Size:                       {file_path.stat().st_size / 1024 :.2f} kb")


if __name__ == "__main__":
    main()
