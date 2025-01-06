"""

Write a Python program that takes three integers and checks whether the sum of the last digit of the first number
and the last digit of the third number equals the last digit of the second number.

Sample Input:
(12, 26, 44)        =>  True
(145, 122, 1010)    =>  False
(0, 20, 40)         =>  True
(1, 22, 40)         =>  False
(145, 129, 104)     =>  True

"""


def main():
    seq = list(map(int, input("Enter a sequence of three integers: ").split()))
    print(str(seq[0] + seq[2])[-1] == str(seq[1])[-1])


if __name__ == "__main__":
    main()
