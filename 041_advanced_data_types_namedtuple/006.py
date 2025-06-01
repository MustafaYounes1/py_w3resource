"""

Write a Python function that takes a Student named tuple as an argument and calculates the average grade.

Student(name="Ain Ruth", age=22, marks=[89, 92, 75, 90, 86])    ->  86.4

"""

from statistics import mean
from typing import Callable, NamedTuple


class Student(NamedTuple):
    name: str
    age: int
    marks: list[int]


def main():
    std = Student(name="Ain Ruth", age=22, marks=[89, 92, 75, 90, 86])
    func: Callable[[Student], float] = lambda s: mean(s.marks)
    print(func(std))


if __name__ == "__main__":
    main()
