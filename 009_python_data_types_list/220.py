"""

Write a Python program to map the values of a list to a dictionary using a function, where the key-value pairs consist
of the original value as the key and the result of the function as the value.

[1, 2, 3], square the values

{1: 1, 2: 4, 3: 9}

"""


def main():
    lst = [1, 2, 3]
    print(dict(zip(lst, map(lambda x: pow(x, 2), lst))))


if __name__ == "__main__":
    main()
