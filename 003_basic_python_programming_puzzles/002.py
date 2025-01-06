"""

Write a Python program that accepts a list of integers and calculates the length and the fifth element.
Return true if the length of the list is 8 and the fifth element occurs thrice in the said list.

[19, 19, 15, 5, 5, 5, 1, 2]         =>  True
[19, 15, 5, 7, 5, 5, 2]             =>  False
[11, 12, 14, 13, 14, 13, 15, 14]    =>  True
[19, 15, 11, 7, 5, 6, 2]            =>  False

"""


def main():
    seq = list(map(int, input("Enter a list of comma-separated integers: ").split(", ")))
    print(len(seq) == 8 and seq.count(seq[4]) == 3)


if __name__ == "__main__":
    main()
