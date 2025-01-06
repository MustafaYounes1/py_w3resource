"""

 Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three
 occurrences of five. Return True otherwise False.

[19, 19, 15, 5, 3, 5, 5, 2]     =>  True
[19, 15, 15, 5, 3, 3, 5, 2]     =>  False
[19, 19, 5, 5, 5, 5, 5]         =>  True

"""


def main():
    seq = list(map(int, input("Enter a list of comma-separated integers: ").split(", ")))
    print(seq.count(19) == 2 and seq.count(5) >= 3)


if __name__ == "__main__":
    main()
