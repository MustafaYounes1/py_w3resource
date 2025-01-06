"""

Write a Python program that removes duplicate elements from a given array of numbers so that each element appears
only once and returns the new length of the array.

Sample Input:
[0,0,1,1,2,2,3,3,4,4,4]     =>  5
[1, 2, 2, 3, 4, 4]          =>  4

"""


def main():
    seq = list(map(int, input("Enter a list of space-separated integers: ").split()))
    print(len(set(seq)))


if __name__ == "__main__":
    main()
