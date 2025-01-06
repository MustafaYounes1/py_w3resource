"""

Write a Python program to find all 5's in integers less than n that are divisible by 9 or 15.

Value of n = 50     =>  [[15, 1], [45, 1]]
Value of n = 65     =>  [[15, 1], [45, 1], [54, 0]]
Value of n = 75     =>  [[15, 1], [45, 1], [54, 0]]
Value of n = 85     =>  [[15, 1], [45, 1], [54, 0], [75, 1]]
Value of n = 150    =>  [[15, 1], [45, 1], [54, 0], [75, 1], [105, 2], [135, 2]]

"""


def main():
    n = int(input("Enter a number: "))
    print(
        [
            [_, str(_).index("5")] for _ in range(5, n) if "5" in str(_) and ((_ % 9 == 0) or (_ % 15 == 0))
        ]
    )


if __name__ == "__main__":
    main()
