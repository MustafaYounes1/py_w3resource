"""

Write a Python program to iterate over two lists simultaneously.

num = [1, 2, 3]
color = ['red', 'white', 'black']

1 red
2 white
3 black

"""


def main():
    num = [1, 2, 3]
    color = ['red', 'white', 'black']
    for a, b in zip(num, color):
        print(a, b)


if __name__ == "__main__":
    main()
