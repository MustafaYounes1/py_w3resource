"""

Write a Python function to reverse a string if its length is a multiple of 4.

abcd    =>  dcba
python  =>  python

"""


def main():
    s = input("Enter a string: ")

    if len(s) % 4 == 0:
        print(s[::-1])
    else:
        print(s)


if __name__ == "__main__":
    main()
