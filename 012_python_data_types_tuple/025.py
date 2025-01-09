"""

Write a Python program to convert a given string list to a tuple.

python 3.0

('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')

"""


def main():
    s = "python 3.0"
    print(tuple(s.replace(" ", "")))


if __name__ == "__main__":
    main()
