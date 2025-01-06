"""

Write a Python program to iterate a given list cyclically at a specific index position.

['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

3   =>  ['d', 'e', 'f', 'g', 'h', 'a', 'b', 'c']
5   =>  ['f', 'g', 'h', 'a', 'b', 'c', 'd', 'e']

"""


def main():
    lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    indices = (3, 5)

    for idx in indices:
        print(lst[idx:] + lst[0:idx])


if __name__ == "__main__":
    main()
