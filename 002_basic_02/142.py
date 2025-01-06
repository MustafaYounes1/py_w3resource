"""

 Write a Python program to check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones
 of the same length in a given string. Return True/False.

Original sequence: 001011           =>  False
Original sequence: 01010101         =>  True
Original sequence: 00               =>  False
Original sequence: 000111000111     =>  True
Original sequence: 00011100011      =>  False
Original sequence: 0011101          =>  False

"""

import re


def main():
    s = input("Enter a string of 1s and 0s: ")

    print(
        [len(seq) for seq in re.findall(r"0+", s)] == [len(seq) for seq in re.findall(r"1+", s)]
    )


if __name__ == "__main__":
    main()
