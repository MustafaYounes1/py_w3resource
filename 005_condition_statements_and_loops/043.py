"""

Write a Python program to create the multiplication table (from 1 to 10) of a number.
Expected Output:

Input a number: 6
6 x 1 = 6
6 x 2 = 12
6 x 3 = 18
6 x 4 = 24
6 x 5 = 30
6 x 6 = 36
6 x 7 = 42
6 x 8 = 48
6 x 9 = 54
6 x 10 = 60

"""


def main():
    n = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{n:2d} x {i:2d} = {n * i:2d}")


if __name__ == "__main__":
    main()
