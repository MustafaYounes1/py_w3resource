"""

Write a Python program to create a histogram from a given list of integers.

Sample Input: 2 3 6 5

Output:
======
##
###
######
#####

"""


def main():
    seq = [int(_) for _ in input("Enter a list of space-separated integers: ").split()]
    for _ in seq:
        print("#" * _)


if __name__ == "__main__":
    main()
