"""

Write a Python program to create set left difference.

{'green', 'blue'}
{'yellow', 'blue'}

{'green'}

"""


def main():
    s1 = {'green', 'blue'}
    s2 = {'yellow', 'blue'}
    print(s1 - s2)


if __name__ == "__main__":
    main()
