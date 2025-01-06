"""

Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

Sample value of n is 5
Expected Result : 615  (5 + 55 + 555)

"""


def main():
    n = input("Enter an integer number: ")
    print(int(n) + int(n * 2) + int(n * 3))


if __name__ == "__main__":
    main()
