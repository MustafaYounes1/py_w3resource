"""

Write a Python program to remove all instances of a given value from a given array of integers and find the length
of the newly created array.

Sample Input:
([1, 2, 3, 4, 5, 6, 7, 5], 5)       =>  6
([10,10,10,10,10], 10)              =>  0
([10,10,10,10,10], 20)              =>  5
([], 1)                             =>  0

"""


def main():
    seq = list(map(int, input("Enter a list of space-separated integers: ").split()))
    n = int(input("Enter an integer: "))

    while n in seq:
        seq.remove(n)

    print(len(seq))


if __name__ == "__main__":
    main()
