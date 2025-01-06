"""

Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and
2700 (both included).

"""


def main():
    valid = [n for n in range(1500, 2701) if (n % 7 == 0) and (n % 5 == 0)]
    print(valid)


if __name__ == "__main__":
    main()
