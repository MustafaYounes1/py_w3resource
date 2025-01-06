"""

Write a Python program that removes and prints every third number from a list of numbers until the list is empty
or it has less than 3 elements.

"""


def remove_third(seq):
    try:
        print(seq.pop(2))
        remove_third(seq)

    except IndexError:
        print("The sequence is either empty or has less than 3 elements")


def main():
    seq = [int(_) for _ in input("Enter a list of space-separated integers: ").split()]
    remove_third(seq)


if __name__ == "__main__":
    main()
