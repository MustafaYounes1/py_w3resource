"""

Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.

"""


def main():
    seq = [int(_) for _ in input("Enter three space-separated integers: ").split()]
    if len(set(seq)) == 2:
        print(0)
    else:
        print(sum(seq))


if __name__ == "__main__":
    main()
