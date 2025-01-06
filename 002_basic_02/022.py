"""

Write a Python program to create a sequence where the first four members of the sequence are equal to one.

Each successive term of the sequence is equal to the sum of the four previous ones. Find the Nth member of the sequence.

    5   =>  4
    6   =>  7
    7   =>  13

"""


def find_nth(n):
    if n <= 4:
        return 1

    return find_nth(n - 1) + find_nth(n - 2) + find_nth(n - 3) + find_nth(n - 4)


def main():
    n = int(input("Enter a number: "))
    print(find_nth(n))


if __name__ == "__main__":
    main()
