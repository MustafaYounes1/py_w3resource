"""

Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.

"""

from string import ascii_uppercase


def main():
    for _ in ascii_uppercase:
        with open(f"{_}.txt", "w") as f:
            f.write(f"The contents of {_} file\n")


if __name__ == "__main__":
    main()
