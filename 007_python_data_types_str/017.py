"""

Write a Python function to get a string made of 4 copies of the last two characters of a specified string
(length must be at least 2).

Sample function and result :
insert_end('Python') -> onononon
insert_end('Exercises') -> eseseses

"""


def main():
    s = input("Enter a string: ")
    print(s[-2:] * 4)


if __name__ == "__main__":
    main()
