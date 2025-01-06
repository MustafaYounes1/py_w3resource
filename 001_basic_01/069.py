"""

Write a Python program to sort three integers without using conditional statements and loops.

"""


def main():
    seq = [int(_) for _ in input("Enter three space-separated integers: ").split()]
    print(sorted(seq))


if __name__ == "__main__":
    main()
