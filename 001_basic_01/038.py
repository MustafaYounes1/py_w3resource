"""

Write a Python program to solve (x + y) * (x + y).

Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49

"""


def main():
    x, y = [int(_) for _ in input("Enter x and y (space-separated): ").split()]
    print(pow((x + y), 2))


if __name__ == "__main__":
    main()
