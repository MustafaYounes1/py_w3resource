"""

Write a Python program to create a symmetric difference.

{'blue', 'green'}
{'blue', 'yellow'}

{'green', 'yellow'}

"""


def main():
    s1 = {'blue', 'green'}
    s2 = {'blue', 'yellow'}
    print(s1 ^ s2)


if __name__ == "__main__":
    main()
