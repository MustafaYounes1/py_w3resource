"""

Write a Python program to traverse a given list in reverse order, and print the elements with the original index.

['red', 'green', 'white', 'black']

3 black
2 white
1 green
0 red

"""


def main():
    lst = ['red', 'green', 'white', 'black']
    for idx, _ in reversed(list(enumerate(lst))):
        print(f"{idx} {_}")


if __name__ == "__main__":
    main()
