"""

Write a Python program to find the highest and lowest number from a given string of space-separated integers.

Original string: 1 4 5 77 9 0       =>  (77, 0)
Original string: -1 -4 -5 -77 -9 0  =>  (0, -77)
Original string: 0 0                =>  (0, 0)

"""


def main():
    seq = list(map(int, input("Enter a list of space separated integers: ").split()))
    print((max(seq), min(seq)))


if __name__ == "__main__":
    main()
