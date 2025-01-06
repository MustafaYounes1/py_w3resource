"""

Write a Python program to check if a given string contains two similar consecutive letters.

Original string: PHP    =>  False
Original string: PHHP   =>  True
Original string: PHPP   =>  True

"""


def main():
    s = input("Enter a string: ")
    for l1, l2 in zip(s, s[1:]):
        if l1 == l2:
            print(True)
            exit(0)

    print(False)


if __name__ == "__main__":
    main()
