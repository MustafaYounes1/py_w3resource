"""

Write a Python program to find a list of integers containing exactly four distinct values, such that no integer
repeats twice consecutively

[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]    =>  True
[1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]    =>  False
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]       =>  False

"""


def main():
    seq = list(map(int, input("Enter a list of comma-separated integers: ").split(", ")))
    print(len(set(seq)) == 4 and all([a != b for a, b in zip(seq, seq[1:])]))


if __name__ == "__main__":
    main()
