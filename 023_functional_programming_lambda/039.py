"""

Write a Python program to find the elements of a given list of strings that contain a specific substring using lambda.

['red', 'black', 'white', 'green', 'orange']

ack     =>  ['black']
abc     =>  []

"""

from typing import Callable


def main():
    lst = ['red', 'black', 'white', 'green', 'orange']
    f: Callable[[list[str], str], list[str]] = lambda ll, ss: list(filter(lambda _: ss in _, ll))
    print(f(lst, "ack"))
    print(f(lst, "abc"))


if __name__ == "__main__":
    main()
