"""

Write a Python program to swap commas and dots in a string.

Sample string: "32.054,23"
Expected Output: "32,054.23"

"""


def main():
    s = "32.054,23"
    print(s.translate(str.maketrans(".,", ",.")))


if __name__ == "__main__":
    main()
