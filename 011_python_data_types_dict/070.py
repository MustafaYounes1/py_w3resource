"""

Write a Python program to map the values of a given list to a dictionary using a function, where the key-value pairs
consist of the original value as the key and the result of the function as the value.

[1, 2, 3, 4], lambda x: x * x

{1: 1, 2: 4, 3: 9, 4: 16}

"""


def main():
    lst, func = [1, 2, 3, 4], lambda x: x * x
    print(dict(zip(lst, map(func, lst))))


if __name__ == "__main__":
    main()
