"""

Write a Python program to find the sublist of numbers from a given list of numbers with only odd digits in
increasing order.

[1, 3, 79, 10, 4, 2, 39]                =>  [1, 3, 39, 79]
[11, 31, 40, 68, 77, 93, 48, 1, 57]     =>  [1, 11, 31, 57, 77, 93]
[9, -2, 3, 4, -2, 0, 2, -3, 8, -1]      =>  [-3, -1, 3, 9]
"""


def main():
    seq = list(map(int, input("Enter a list of comma-separated integers: ").split(",")))
    print(
        sorted(n for n in seq if all(int(c) % 2 for c in str(abs(n))))
    )


if __name__ == "__main__":
    main()
