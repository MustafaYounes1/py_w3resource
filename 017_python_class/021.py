"""

Write a Python class that has two methods: get_string and print_string , get_string accept a string from the user
and print_string prints the string in upper case.

"""


class Solver:
    __str = ""

    @classmethod
    def get_string(cls) -> None:
        cls.__str = input("Please enter a string: ")

    @classmethod
    def print_string(cls) -> None:
        print(cls.__str.upper())


def main():
    Solver.get_string()
    Solver.print_string()


if __name__ == "__main__":
    main()
