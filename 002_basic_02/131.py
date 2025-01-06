"""

Write a Python program to count the number of zeros and ones in the binary representation of a given integer.

Original number: 12     =>  Number of zeros: 2, Number of ones: 2
Original number: 1234   =>  Number of zeros: 6, Number of ones: 5

"""


def main():
    n = int(input("Enter a number: "))
    n = f"{n:b}"
    print(f"0s = {n.count('0')}, 1s: {n.count('1')}")


if __name__ == "__main__":
    main()
