"""

Write a Python program to find the number which when appended to the list makes the total 0.

[1, 2, 3, 4, 5]                                         =>  -15
[-1, -2, -3, -4, 5]                                     =>  5
[10, 42, 17, 9, 1315182, 184, 102, 29, 15, 39, 755]     =>  -1316384

"""


def main():
    seq = list(map(int, input("Enter a list of comma-separated integers: ").split(",")))
    print(-sum(seq))


if __name__ == "__main__":
    main()
