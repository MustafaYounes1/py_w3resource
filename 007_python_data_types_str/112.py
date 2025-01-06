"""

Write a Python program to calculate the sum of two numbers given as strings. Return the result in the same
string representation.

234242342341, 2432342342    -> "236674684683"
"", 2432342342              -> False
1000, 0                     -> "1000"
1000, 10                    -> "1010"

"""


def main():
    try:
        n1, n2 = input("Enter two comma-separated numbers: ").split(", ")
        n1, n2 = int(n1), int(n2)
        print(n1 + n2)

    except ValueError:
        print(False)


if __name__ == "__main__":
    main()
