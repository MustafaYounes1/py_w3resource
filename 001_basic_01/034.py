"""

Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.

"""


def main():
    n1, n2 = [int(_) for _ in input("Enter two space-separated integers: ").split()]
    s = n1 + n2
    if 20 > s > 15:
        print(20)
    else:
        print(s)


if __name__ == "__main__":
    main()
