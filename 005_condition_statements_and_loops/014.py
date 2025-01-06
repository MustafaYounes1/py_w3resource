"""

Write a Python program that accepts a string and calculates the number of digits and letters.
Sample Data : Python 3.2
Expected Output :
Letters 6
Digits 2

"""



def main():
    s = input("Enter a string: ")
    l, d = [], []

    for _ in s:
        if _.isalpha():
            l.append(_)

        elif _.isdigit():
            d.append(_)

        else:
            pass

    print(f"Number of letters: {len(l)}")
    print(f"Number of digits: {len(d)}")


if __name__ == "__main__":
    main()
