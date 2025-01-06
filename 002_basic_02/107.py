"""

Write a Python program to check whether a given number is "Oddish" or "Evenish".

A number is called "Oddish" if the sum of all of its digits is odd, and a number is called "Evenish" if the sum of all
of its digits is even.

Sample Output:
Original Number 120     =>  Oddish
Original Number 321     =>  Evenish
Original Number 43      =>  Oddish
Original Number 4433    =>  Evenish
Original Number 373     =>  Oddish

"""


def main():
    n = input("Enter a number: ")
    res = sum(list(map(int, n)))

    if res % 2 == 0:
        print("Evenish")
    else:
        print("Oddish")


if __name__ == "__main__":
    main()
