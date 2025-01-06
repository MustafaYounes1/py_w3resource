"""

A valid filename should end in .txt, .exe, .jpg, .png, or .dll, and should have at most three digits,
no additional periods.

Write a Python program to create a list of True/False that determine whether candidate filename is valid or not.

Input:
['abc.txt', 'windows.dll', 'tiger.png', 'rose.jpg', 'test.py', 'win32.exe']
Output:
['Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes']

Input:
['.txt', 'windows.exe', 'tiger.jpeg', 'rose.c', 'test.java']
Output:
['No', 'Yes', 'No', 'No', 'No']

"""

from pathlib import Path

__data = [
    ['abc.txt', 'windows.dll', 'tiger.png', 'rose.jpg', 'test.py', 'win32.exe'],
    ['.txt', 'windows.exe', 'tiger.jpeg', 'rose.c', 'test.java']
]

__valid_sfx = {".txt", ".exe", ".jpg", ".png", ".dll"}


def main():
    for sample in __data:
        print(
            ["Yes" if Path(_).suffix in __valid_sfx else "No" for _ in sample]
        )


if __name__ == "__main__":
    main()
