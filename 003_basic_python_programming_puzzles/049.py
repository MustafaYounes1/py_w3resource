"""

Write a Python program to find the h-index, the largest positive number h such that h occurs in the sequence at
least h times. If there is no such positive number return h = -1.

[1, 2, 2, 3, 3, 4, 4, 4, 4]                             =>  4
[1, 2, 2, 3, 4, 5, 6]                                   =>  2
[3, 1, 4, 17, 5, 17, 2, 1, 41, 32, 2, 5, 5, 5, 5]       =>  5

"""


def main():
    seq = list(map(int, input("Enter a list of comma-separated integers: ").split(",")))
    print(max([-1] + [i for i in seq if 0 < i <= seq.count(i)]))


if __name__ == "__main__":
    main()
