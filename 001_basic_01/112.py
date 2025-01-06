"""

Write a Python program to remove the first item from a specified list.

"""


def main():
    seq = [int(_) for _ in input("Enter a list of space-separated integers: ").split()]
    seq.pop(0)
    print(seq)


if __name__ == "__main__":
    main()
