"""

Write a Python program to test whether a given number is symmetrical or not. A number is symmetrical when it is equal
to its reverse. A number is symmetrical when it is equal of its reverse.
Sample Input:
(121)       =>  True
(0)         =>  True
(122)       =>  False
(990099)    =>  True

"""


def main():
    n = input("Enter the number: ")
    print(n == n[-1::-1])


if __name__ == "__main__":
    main()
