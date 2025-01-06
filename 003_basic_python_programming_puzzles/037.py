"""

Write a Python program to find the largest integer divisor of a number n that is less than n.

Input: 18       =>  9
Input: 100      =>  50
Input: 102      =>  51
Input: 500      =>  250
Input: 1000     =>  500
Input: 6500     =>  3250

"""


def main():
    n = int(input("Enter a number: "))
    for _ in range(n - 1, 0, -1):
        if (n % _) == 0:
            print(_)
            break



if __name__ == "__main__":
    main()
