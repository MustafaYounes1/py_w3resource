"""

Write a Python program to find the shortest distance from a specified character in a given string. Return the
shortest distances through a list and use an itertools component to solve the problem.

"r", "w3resource"           =>  [2, 1, 0, 1, 2, 2, 1, 0, 1, 2]
"e", "python exercises"     =>  [7, 6, 5, 4, 3, 2, 1, 0, 1, 0, 1, 2, 2, 1, 0, 1]
"S", "JavaScript"           =>  [4, 3, 2, 1, 0, 1, 2, 3, 4, 5]

"""

from itertools import chain


def main():
    data = [
        ("r", "w3resource"),
        ("e", "python exercises"),
        ("S", "JavaScript"),
    ]

    for c, w in data:
        res = [len(w)] * len(w)
        prev_i = -len(w)

        for i in chain(range(len(w)), reversed(range(len(w)))):
            if c == w[i]:
                prev_i = i
            res[i] = min(res[i], abs(i - prev_i))

        print(res)


if __name__ == "__main__":
    main()
