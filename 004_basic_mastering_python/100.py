"""

Replace all occurrences of a substring in a string.

s = "Hello world, welcome to the world of Python family."
Replace all occurrences of 'world' with 'universe'

Hello universe, welcome to the universe of Python family.

"""


def main():
    s = "Hello world, welcome to the world of Python family."
    print(s.replace("world", 'universe'))


if __name__ == "__main__":
    main()
