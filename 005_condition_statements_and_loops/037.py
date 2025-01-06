"""

Write a Python program that reads a month and prints the season for that month.
Expected Output:

Input the month (e.g. January, February etc.): April
Season is Spring

"""


def main():
    m = input("Enter the month: ")

    if m.lower() in "december january february".split():
        print("Winter")

    elif m.lower() in "march april may".split():
        print("Spring")

    elif m.lower() in "june july august".split():
        print("Summer")

    else:
        print("Autumn")


if __name__ == "__main__":
    main()
