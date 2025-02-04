"""

Write a Python program that accepts a sequence of comma-separated numbers from the user and generates
a list and a tuple of those numbers.

Sample data : 3, 5, 7, 23

Output :
========
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')

"""


def main():
    seq = input("Enter a sequence of comma-separated integer numbers: ")
    print(f"List: {seq.split(',')}")
    print(f"Tuple: {tuple(seq.split(','))}")


if __name__ == "__main__":
    main()
