"""

Write a Python program to filter positive numbers from a list.

"""


def main():
    seq = [int(_) for _ in input("Enter a list of space-separated integers: ").split()]
    print(list(filter(lambda x: x > 0, seq)))


if __name__ == "__main__":
    main()
