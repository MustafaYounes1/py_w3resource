"""

Write a Python program to convert all the characters into uppercase and lowercase and eliminate duplicate letters
from a given sequence. Use the map() function.

['a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a']
[('E', 'e'), ('A', 'a'), ('O', 'o'), ('B', 'b'), ('U', 'u'), ('F', 'f'), ('I', 'i')]

"""


def main():
    lst = ['a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a']
    print(list(map(lambda _: (_.upper(), _.lower()), set(lst))))


if __name__ == "__main__":
    main()
