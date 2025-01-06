"""

Write a Python program that returns a string that is n (non-negative integer) copies of a given string.

"""


def main():
    string = "A test string!"
    n = int(input("Enter a non-negative integer: "))
    assert n >= 0, "Expected a non-negative integer"
    print(string * n)


if __name__ == "__main__":
    main()
