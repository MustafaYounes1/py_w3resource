"""

Write a Python program to find the closest palindrome number to a given integer. If there are two palindrome numbers
in absolute distance return the smaller number.

Note: An integer is a palindrome when it reads the same backward as forward. Negative numbers are not palindromic.

Original number: 120    =>  121
Original number: 321    =>  323
Original number: 43     =>  44
Original number: 1234   =>  1221

"""


def find_closest_palindrome(n):
    # Initialize two variables 'x' and 'y' to the original value of 'n'.
    x = n
    y = n

    # Loop indefinitely until a palindrome is found.
    while True:
        # Check if the string representation of 'x' is a palindrome.
        if str(x) == str(x)[::-1]:
            # If 'x' is a palindrome, return it as the closest palindrome.
            return x

        # Decrement 'x' by 1 for the next iteration.
        x -= 1

        # Check if the string representation of 'y' is a palindrome.
        if str(y) == str(y)[::-1]:
            # If 'y' is a palindrome, return it as the closest palindrome.
            return y

        # Increment 'y' by 1 for the next iteration.
        y += 1


def main():
    n = int(input("Enter a number: "))
    print(find_closest_palindrome(n))


if __name__ == "__main__":
    main()
