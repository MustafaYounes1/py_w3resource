"""

Write a Python program to implement a generator function that generates the running average of a sequence of numbers.

[5, 6, 7]           =>  +5.00 +5.50 +6.00
[-1, -2, -3, -4]    =>  -1.00 -1.50 -2.00 -2.50

"""

from typing import Generator


def moving_avg() -> Generator[float, float | int, None]:
    cnt, total = 0, 0

    while True:
        sent_val = yield total / cnt if cnt else 0
        if isinstance(sent_val, int | float):
            total += sent_val
            cnt += 1


def main():
    data = [
        [5, 6, 7],
        [-1, -2, -3, -4]
    ]

    for lst in data:
        gen = moving_avg()
        next(gen)  # start the generator before using .send

        for _ in lst:
            print(f"{gen.send(_):+4.2f}", end=" ")

        print()


if __name__ == "__main__":
    main()
