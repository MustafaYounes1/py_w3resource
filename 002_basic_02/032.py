"""

Write a Python program to find the heights of the top three buildings in descending order from eight given buildings.

Input:
0 <= height of building (integer) <= 10,000

Input the heights of eight buildings: 25 35 15 16 30 45 37 39
Heights of the top three buildings: 45 39 37

"""


def main():
    seq = [int(_) for _ in input("Enter a list of space-separated integers: ").split()]
    print(sorted(seq, reverse=True)[:3])


if __name__ == "__main__":
    main()
