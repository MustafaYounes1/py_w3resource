"""

Write a Python program to count the number of even and odd numbers in a series of numbers

Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
Expected Output :
Number of even numbers : 4
Number of odd numbers : 5

"""


def main():
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    odds, evens = [], []

    for _ in numbers:
        if _ % 2 == 0:
            evens.append(_)
        else:
            odds.append(_)

    print(f"Number of even numbers: {len(evens)}")
    print(f"Number of odd numbers: {len(odds)}")


if __name__ == "__main__":
    main()
