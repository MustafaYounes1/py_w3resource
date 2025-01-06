"""

Write a Python program to find the sum of the even elements that are at odd indices in a given list.

[1, 2, 3, 4, 5, 6, 7]   =>  12
[1, 2, 8, 3, 9, 4]      =>  6

"""


def main():
    seq = list(map(int, input("Enter a list of comma-separated integers: ").split(",")))
    print(
        sum([seq[_] for _ in range(1, len(seq), 2) if seq[_] % 2 == 0])
    )


if __name__ == "__main__":
    main()
