"""

Write a Python program to find the last occurrence of a specified item in a given list.

['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']

Last occurrence of f    =>  7
Last occurrence of c    =>  15
Last occurrence of k    =>  14
Last occurrence of w    =>  12

"""


def main():
    lst = ['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
    chars = ['f', 'c', 'k', 'w']

    for _ in chars:
        print("".join(lst).rfind(_))


if __name__ == "__main__":
    main()
