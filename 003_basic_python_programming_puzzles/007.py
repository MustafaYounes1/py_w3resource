"""

Write a Python program to check a given list of integers where the sum of the first i integers is i.

[0, 1, 2, 3, 4, 5]  =>  False
[1, 1, 1, 1, 1, 1]  =>  True
[2, 2, 2, 2, 2]     =>  False

"""

from itertools import accumulate
from operator import add


def main():
    seq = list(map(int, input("Enter a list of comma-separated integers: ").split(", ")))
    print(list(accumulate(seq, add)) == list(range(1, len(seq) + 1)))


if __name__ == "__main__":
    main()
