"""

Write a program that calculates whether a person is eligible for voting based on their age (>= 18) using boolean
conditions.

20  ->  Eligible
18  ->  Eligible
17  ->  Non-eligible

"""

from typing import Literal


def _is_eligible(n: int) -> bool:
    return n >= 18


def can_vote(n: int) -> Literal["Eligible", "Non-eligible"]:
    assert isinstance(n, int), "expected an integer"

    if _is_eligible(n):
        return "Eligible"
    else:
        return "Non-eligible"


def main():
    data = [20, 18, 17]

    for _ in data:
        print(can_vote(_))


if __name__ == "__main__":
    main()
