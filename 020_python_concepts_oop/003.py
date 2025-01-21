"""

Write a Python program to create a calculator class. Include methods for basic arithmetic operations.
e.g. Add, Sub, Mul, Div, True Div

calc.add(5, 5)              =>  10
calc.sub(0, 5)              =>  -5
calc.mul(5.1, 2.3)          =>  11.729999999999999
calc.div(5, 2.0)            =>  2.5
calc.true_div(5, 2.0)       =>  2

"""

from typing import Union


class Calculator:
    @staticmethod
    def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        return a + b

    @staticmethod
    def sub(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        return a - b

    @staticmethod
    def mul(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        return a * b

    @staticmethod
    def div(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        return a / b

    @staticmethod
    def true_div(a: Union[int, float], b: Union[int, float]) -> int:
        return int(a // b)


def main():
    calc = Calculator()

    print(calc.add(5, 5))
    print(calc.sub(0, 5))
    print(calc.mul(5.1, 2.3))
    print(calc.div(5, 2.0))
    print(calc.true_div(5, 2.0))


if __name__ == "__main__":
    main()
