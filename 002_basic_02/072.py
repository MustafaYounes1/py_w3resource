"""

Write a Python program to check whether a given integer is a palindrome or not.
Note: An integer is a palindrome when it reads the same backward as forward. Negative numbers are not palindromic.

Sample Input:
100     =>  False
252     =>  True
-838    =>  False

"""


def main():
    n = input("Enter an integer: ")
    print(n == n[-1::-1])


if __name__ == "__main__":
    main()
