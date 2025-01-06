"""

Write a Python program to find an integer exponent x such that a^x = n.

Input:
a = 2 : n = 1024
Output:
10

Input:
a = 3 : n = 81
Output:
4

Input:
a = 3 : n = 1290070078170102666248196035845070394933441741644993085810116441344597492642263849
Output:
170

"""

from math import log


def main():
    a, n = [float(_) for _ in input("Enter a and n space-separated: ").split()]
    print(log(n, a))


if __name__ == "__main__":
    main()
