"""

Write a Python program to calculate the median from a list of numbers.
Sample Input:
[1,2,3,4,5]                     =>  3
[1,2,3,4,5,6]                   =>  3.5
[6,1,2,4,5,3]                   =>  3.5
[1.0,2.11,3.3,4.2,5.22,6.55]    =>  3.75
[1.0,2.11,3.3,4.2,5.22]         =>  3.3
[2.0,12.11,22.3,24.12,55.22]    =>  22.3

"""

from statistics import median


def main():
    seq = list(map(float, input("Enter a list of space-separated numbers: ").split()))
    print(median(seq))


if __name__ == "__main__":
    main()
