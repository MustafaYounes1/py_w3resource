"""

Write a Python program to create a geometric progression (a^n = a * r^(n-1)) specifying the start element, the end
element, and the step


1, 256, 2   =>  [1, 2, 4, 8, 16, 32, 64, 128, 256]
3, 256, 2   =>  [3, 6, 12, 24, 48, 96, 192]
1, 256, 4   =>  [1, 4, 16, 64, 256]

"""

from math import floor, log
from sys import maxsize


def main():
    data = [
        [1, 256, 2],
        [3, 256, 2],
        [1, 256, 4]
    ]

    for start, end, r in data:
        gen = (start * pow(r, n) for n in range(1, maxsize))
        res = [start]

        while res[-1] * r <= end:
            res.append(next(gen))

        print(res)

        # #Another approach: try to find the number of terms in the sequence floor(log(end / start) / log(step) + 1
        # num_terms = floor(log(end / start) / log(r) + 1)
        # print([start * pow(r, n) for n in range(num_terms)])


if __name__ == "__main__":
    main()
