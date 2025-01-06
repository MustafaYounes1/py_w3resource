"""

Write a Python program to check the following properties of an input path.

    Absolute?
    Is File?
    Is Dir?
    Is Link?        (is a symbolic link)
    Exists?         (if the file path exists (regardless of its type)

"""

import pathlib


def main():
    p = pathlib.Path(input("Enter the path: "))
    print(f"is absolute:    {p.is_absolute()}")
    print(f"is file:        {p.is_file()}")
    print(f"is dir:         {p.is_dir()}")
    print(f"is link:        {p.is_symlink()}")
    print(f"exists:         {p.exists()}")


if __name__ == "__main__":
    main()
