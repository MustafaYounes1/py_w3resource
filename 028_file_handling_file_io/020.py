"""

Write a Python program to create a file where all letters of English alphabet are listed by specified number of
letters on each line.

    Out file: "020.txt"
    Each line should hold 3 letters at most

"""

from string import ascii_uppercase

__out_f_path = "020.txt"


def main():
    n = 3
    with open(__out_f_path, "w") as f:
        for i in range(0, len(ascii_uppercase), n):
            f.write(f"{ascii_uppercase[i: i + n]}\n")


if __name__ == "__main__":
    main()
