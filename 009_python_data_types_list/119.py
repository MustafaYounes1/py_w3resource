"""

Write a Python program to check if a substring appears in a given list of string values.

['red', 'black', 'white', 'green', 'orange']

ack     =>  True
abc     =>  False

"""


def main():
    lst = ['red', 'black', 'white', 'green', 'orange']
    print(any('ack' in _ for _ in lst))
    print(any('abc' in _ for _ in lst))


if __name__ == "__main__":
    main()
