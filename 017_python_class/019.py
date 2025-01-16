"""

Write a Python class to implement pow(x, n).

2, -3   =>  0.125
3, 5    =>  243
100, 0  =>  1

"""

from typing import Union


class Power:
    @classmethod
    def solve(cls, x: int, n: int) -> Union[int, float]:
        res = 1

        for _ in range(abs(n)):
            res *= x

        if n >= 0:
            return res
        else:
            return 1 / res


def main():
    print(Power.solve(2, -3))
    print(Power.solve(3, 5))
    print(Power.solve(100, 0))


if __name__ == "__main__":
    main()
