"""

Write a Python program to find an increasing sequence consisting of the elements of the original list.

[1, 3, 79, 10, 4, 2, 39]                =>  [1, 2, 3, 4, 10, 39, 79]
[11, 31, 40, 68, 77, 93, 48, 1, 57]     =>  [1, 11, 31, 40, 48, 57, 68, 77, 93]
[9, -2, 3, 4, -2, 0, 2, -3, 8, -1]      =>  [-3, -2, -1, 0, 2, 3, 4, 8, 9]

"""


def main():
    seq = list(map(int, input("Enter a list of comma-separated integers: ").split(",")))
    print(sorted(set(seq)))


if __name__ == "__main__":
    main()
