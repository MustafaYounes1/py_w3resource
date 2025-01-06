"""

Write a Python program to sum two integers. However, if the sum is between 15 and 20 it will return 20.

"""


def main():
    n1, n2 = list(map(int, input("Enter two space-separated integers: ").split()))
    s = 20 if 15 <= n1 + n2 <= 20 else n1 + n2
    print(s)


if __name__ == "__main__":
    main()
