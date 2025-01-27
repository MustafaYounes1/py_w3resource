"""

Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
    sorted positives (ascending order) -> sorted negatives (ascending order)

[-1, 2, -3, 5, 7, 8, 9, -10]    =>  [2, 5, 7, 8, 9, -10, -3, -1]

"""


def main():
    lst = [-1, 2, -3, 5, 7, 8, 9, -10]
    print(sorted(lst, key=lambda _: 0 if not _ else -1/_))


if __name__ == "__main__":
    main()
