"""

Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are
not numerical.

"""


def main():
    try:
        n1, n2 = list(map(int, input("Enter two space separated numbers: ").split()))
        print(n1, n2)

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
