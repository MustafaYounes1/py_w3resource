"""

Write a Python class to reverse a string word by word.

'hello .py'     =>  '.py hello'

"""


class Solver:
    @classmethod
    def solve(cls, s: str) -> str:
        return " ".join(s.split()[::-1])


def main():
    print(Solver.solve("hello .py"))


if __name__ == "__main__":
    main()
