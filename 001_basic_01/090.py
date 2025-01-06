"""

Write a Python program to create a copy of its own source code.

"""

OUT_FILE = "090_copy.py"


def main():
    with open(__file__, "r") as src, open(OUT_FILE, 'w') as dst:
        contents = src.readlines()
        for _ in contents:
            dst.write(f"{_}")


if __name__ == "__main__":
    main()
