"""

A Python list contains three positive integers. Write a Python program to check whether the sum of the digits in
each number is equal or not. Return true otherwise false.

Sample Data:
([13, 4, 22]) -> True
([-13, 4, 22]) -> False
([45, 63, 90]) -> True

"""


def main():
    seq = list(map(int, input("Enter a list of comma-separated integers: ").split(", ")))
    print(seq[0] % 9 == seq[1] % 9 == seq[2] % 9)


if __name__ == "__main__":
    main()
