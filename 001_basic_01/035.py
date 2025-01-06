"""

 Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.

"""


def main():
    n1, n2 = [int(_) for _ in input("Enter two space-separated integers: ").split()]
    if (n1 == n2) or ((n1 + n2) == 5) or (abs(n1 - n2) == 5):
        print(True)
    else:
        print(False)


if __name__ == "__main__":
    main()
