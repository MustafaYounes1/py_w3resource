"""

Write a Python program that takes a string and replaces all the characters with their respective numbers.

Python              -> "16 25 20 8 15 14"
Java                -> "10 1 22 1"
Python Tutorial     -> "16 25 20 8 15 14 20 21 20 15 18 9 1 12"

"""


def main():
    s = input("Enter a string: ")
    print(" ".join([str(ord(_.lower()) - ord("a") + 1) for _ in s.replace(" ", "")]))


if __name__ == "__main__":
    main()
