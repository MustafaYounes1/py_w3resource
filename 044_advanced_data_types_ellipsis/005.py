"""

Write a Python program to create a generator expression that generates a sequence of numbers with ellipsis
representing skipped values.

    Args:
        start (int): The starting value of the sequence.
        end (int): The ending value of the sequence.
        step (int): The step size between values.
        skip_count (int): The number of values to skip with ellipsis. (yield skip_count items, and then skip skip_count items)

    Returns:
        A generator expression for the sequence.

generate_sequence(1, 30, 2, 4)
    ->  1, 3, 5, 7, ..., 11, 13, 15, 17, ..., 21, 23, 25, 27, ...,

"""

from typing import Generator


def generate_with_skips(s: int, e: int, step: int, skip_cnt: int) -> Generator[int | str, None, None]:
    cnt = skip_cnt
    for i in range(s, e, step):
        if cnt > 0:
            yield i
            cnt -= 1
        else:
            yield "..."
            cnt = skip_cnt


def main():
    for itm in generate_with_skips(1, 30, 2, 4):
        print(itm, end=", ")


if __name__ == "__main__":
    main()
