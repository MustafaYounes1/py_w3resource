"""

Write a Python program that counts the number of leap years within the range of years.
Ranges of years should be accepted as strings.

1981-1991 -> 2
2000-2020 -> 6

"""


def main():
    y1, y2 = input("Enter the range dash-separated: ").split('-')
    print(len([_ for _ in range(int(y1), int(y2) + 1) if _ % 4 == 0]))


if __name__ == "__main__":
    main()
