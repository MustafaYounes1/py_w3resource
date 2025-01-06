"""

Write a Python program to count the number of equal numbers from three given integers.

Sample Input:
(1, 1, 1)       =>  3
(1, 2, 2)       =>  2
(-1, -2, -3)    =>  0
(-1, -1, -1)    =>  3

"""


def main():
    seq = list(map(int, input("Enter a list of 3 space-separated integers: ").split()))
    s = set(seq)
    print(len(seq) - len(s) + 1 if len(seq) != len(s) else 0)


if __name__ == "__main__":
    main()
