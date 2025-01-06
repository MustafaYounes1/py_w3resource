"""

Write a Python program to calculate the average of the numbers a through b (b not included) rounded to the nearest
integer, in binary (or -1 if there are no such numbers).

4 , 7      =>  0b101
11 , 19    =>  0b1110

"""

from statistics import mean


def main():
    a, b = [int(_) for _ in input("Enter a, b space-separated: ").split()]
    vals = list(range(min(a, b), max(a, b)))
    if vals:
        print(bin(round(mean(vals))))
    else:
        print(-1)


if __name__ == "__main__":
    main()
