"""

Write a Python program that takes a positive integer and creates an N x N square filled with the integer N.
Display the N x N square.

Sample Data:
(2) -> [[2, 2], [2, 2]]
(5) -> [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]
(-6) -> []

"""


def main():
    n = int(input("Enter a number: "))
    print(
        [
            [n] * n for _ in range(n)
        ]
    )


if __name__ == "__main__":
    main()
