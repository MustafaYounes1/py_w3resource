"""

Write a Python program to check whether a given employee code is exactly 8 digits or 12 digits.
Return True if the employee code is valid and False if it's not.

Sample Input:
('12345678')        =>  True
('1234567j')        =>  False
('12345678j')       =>  False
('123456789123')    =>  True
('123456abcdef')    =>  False

"""


def main():
    code = input("Enter the code: ")
    print(code.isdigit() and len(code) in (8, 12))


if __name__ == "__main__":
    main()
