"""

15. Write a Python program to check the priority of the four operators (+, -, *, /).

    print(test_higher_priority('*','-'))
    print(test_higher_priority('+','-'))
    print(test_higher_priority('+','*'))
    print(test_higher_priority('+','/'))
    print(test_higher_priority('*','/'))

Output:
    True
    True
    False
    False
    True

"""


__priority = {
    "+": 0,
    "-": 0,
    "*": 1,
    "/": 1
}


def t(operator1, operator2):
    return __priority[operator1] >= __priority[operator2]


def main():
    print(t('*', '-'))
    print(t('+', '-'))
    print(t('+', '*'))
    print(t('+', '/'))
    print(t('*', '/'))


if __name__ == "__main__":
    main()
