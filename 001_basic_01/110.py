"""

Write a Python program to get numbers divisible by fifteen from a list using an anonymous function.

"""


def main():
    seq = [int(_) for _ in input("Enter a list of space-separated integers: ").split()]
    print(list(filter(lambda x: x % 15 == 0, seq)))


if __name__ == "__main__":
    main()
