"""

Write a Python program to find an integer (n >= 0) with the given number of even and odd digits.

Note: allowed digits are 2 and 3 and let the evens first

Number of even digits: 2 ,Number of odd digits: 3       =>  22333
Number of even digits: 4 ,Number of odd digits: 7       =>  22223333333

"""


def main():
    e, o = [int(_) for _ in input("Enter the number of 2s and number of 3s space-separated: ").split()]
    print(int(e * "2" + o * "3"))


if __name__ == "__main__":
    main()
