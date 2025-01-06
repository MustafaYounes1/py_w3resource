"""

Write a Python program to convert a given decimal number to a binary list.

Original Number: 8      =>  [1, 0, 0, 0]
Original Number: 45     =>  [1, 0, 1, 1, 0, 1]
Original Number: 100    =>  [1, 1, 0, 0, 1, 0, 0]

"""


def main():
    nums = [8, 45, 100]
    for n in nums:
        print(list(map(int, f"{n:b}")))


if __name__ == "__main__":
    main()
