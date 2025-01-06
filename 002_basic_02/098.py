"""

Write a Python program to check whether a sequence of numbers has an increasing trend or not.

Sample Input:
[1,2,3,4]       =>  True
[1,2,5,3,4]     =>  False
[-1,-2,-3,-4]   =>  False
[-4,-3,-2,-1]   =>  True
[1,2,3,4,0]     =>  False

"""


def check(seq):
    return sorted(seq) == seq


def main():
    seq = list(map(int, input("Enter a list of space-separated numbers: ").split()))
    print(check(seq))


if __name__ == "__main__":
    main()
