"""

Write a Python program to check whether the average value of the elements of a given array of numbers is a whole
number or not.

1 3 5 7 9       =>  True
2 4 2 6 4 8     =>  False

"""

from statistics import mean


def main():
    seq = list(map(int, input("Enter a list of space-separated numbers: ").split()))
    print(float(mean(seq)).is_integer())


if __name__ == "__main__":
    main()
