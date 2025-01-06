"""

Write a Python program that accepts an integer and determines whether it is greater than 4^4 and which is 4 mod 34.

922     =>  True
914     =>  False
854     =>  True

"""


def main():
    n = int(input("Enter a number: "))
    print(n > pow(4, 4) and (n % 34) == 4)


if __name__ == "__main__":
    main()
