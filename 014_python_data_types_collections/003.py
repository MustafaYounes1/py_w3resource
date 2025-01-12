"""

Write a Python program to create a new deque with the items 'aeiou' and iterate over the deque's elements.

a e i o u

"""

from collections import deque


def main():
    d = deque('aeiou')
    for _ in d:
        print(_, end=" ")


if __name__ == "__main__":
    main()
