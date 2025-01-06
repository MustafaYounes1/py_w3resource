"""

Write a Python program that determines the difference between the largest and smallest integers created by 8 numbers
from 0 to 9. The number that can be rearranged shall start with 0 as in 00135668.

Input:
Input an integer created by 8 numbers from 0 to 9.:                                 2345    34568729
Difference between the largest and the smallest integer from the given integer:     3087    75308643

e.g.:
34568729    =>  largest:    98765432    => difference:  75308643
                smallest:   23456789
"""


def main():
    n = input("Enter the number: ")
    smallest = "".join(sorted([c for c in n], reverse=False))
    largest = smallest[-1::-1]
    print(int(largest) - int(smallest))


if __name__ == "__main__":
    main()
