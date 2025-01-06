"""

Write a Python program to convert a given number (integer) to a list of digits.

123         =>  [1, 2, 3]
1347823     =>  [1, 3, 4, 7, 8, 2, 3]

"""


def main():
    nums = [123, 1347823]

    for _ in nums:
        print(list(map(int, str(_))))


if __name__ == "__main__":
    main()
