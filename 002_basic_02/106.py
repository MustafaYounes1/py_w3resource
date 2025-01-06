"""

Write a Python program to test whether a given integer is a Pandigital number or not.
From Wikipedia,
In mathematics, a pandigital number is an integer that in a given base has among its significant digits each digit
used in the base at least once.

For example,
1223334444555556666667777777888888889999999990 is a pandigital number in base 10.

The first few pandigital base 10 numbers are given by:
1023456789, 1023456798, 1023456879, 1023456897, 1023456978, 1023456987, 1023457689

1023456897  True
1023456798  True
1023457689  True
1023456789  True
102345679   False

"""

def main():
    n = input("Enter the number: ")
    print(len(set(n)) == 10)


if __name__ == "__main__":
    main()
