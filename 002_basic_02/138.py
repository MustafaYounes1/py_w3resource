"""

Write a Python program to reverse the binary representation of a given number and convert the reversed binary number
into an integer.

Original number: 13     =>  11
Original number: 145    =>  137
Original number: 1342   =>  997

"""


def main():
    n = int(input("Enter a number: "))
    print(int(f"{n:b}"[::-1], 2))


if __name__ == "__main__":
    main()
