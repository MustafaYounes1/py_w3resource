"""

rite a Python program to reverse the digits of a given number and add them to the original.
Repeat this procedure if the sum is not a palindrome.

Note: A palindrome is a word, number, or other sequence of characters which reads the same backward as forward,
such as madam or racecar.

    1234    =>  5555
    1473    =>  9339

"""


def is_palindrome(n):
    return str(n) == str(n)[-1::-1]


def find_palindrome(n):
    while not is_palindrome(n):
        r = int(str(n)[-1::-1])
        n += r

    return n


def main():
    n = int(input("Enter an integer: "))
    print(find_palindrome(n))



if __name__ == "__main__":
    main()
