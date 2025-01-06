"""

Write a Python program that concatenates all elements in a list into a string and returns it.

"""


def main():
    seq = input("Enter a list of space-separated elements: ").split()
    print("".join(seq))


if __name__ == "__main__":
    main()
