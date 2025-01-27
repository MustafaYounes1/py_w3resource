"""

Write a Python program to create a list containing the power of said number in bases raised to the corresponding
number in the index using Python map.

bases_num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

[
    10, 400, 27000, 2560000, 312500000, 46656000000, 8235430000000, 1677721600000000,
    387420489000000000, 100000000000000000000
]

"""


def main():
    bases_num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    indices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list(map(lambda p: pow(p[0], p[1]), zip(bases_num, indices))))


if __name__ == "__main__":
    main()
