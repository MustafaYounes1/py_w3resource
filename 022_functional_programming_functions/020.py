"""

Write a Python program to detect the number of local variables declared in a function.

def f() -> None:
    x = 1
    y = 2
    z = 3

>   3

"""


def f() -> None:
    x = 1
    y = 2
    z = 3


def main():
    print(f.__code__.co_nlocals)


if __name__ == "__main__":
    main()
