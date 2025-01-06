"""

Write a Python program to add two strings as if they were numbers (positive integer values). Return a message if
the numbers are strings.

10 32       =>  42
10 22.6    =>  Error in input!
100 -200   =>  Error in input!

"""


def main():
    try:
        n1, n2 = input("Enter two numbers space-separated: ").split()
        n1, n2 = int(n1), int(n2)
        assert n1 >= 0 and n2 >= 0, "Expected positive numbers"
        print(n1 + n2)

    except ValueError and AssertionError:
        print("Error in input")


if __name__ == "__main__":
    main()
