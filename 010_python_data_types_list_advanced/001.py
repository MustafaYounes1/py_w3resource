"""

Write a Python function to reverse a list at a specific location.

[10, 20, 30, 40, 50, 60, 70, 80]

start_pos = 2
end_pos = 4
=>  [10, 20, 50, 40, 30, 60, 70, 80]

start_pos = 6
end_pos = 7
=>  [10, 20, 30, 40, 50, 60, 80, 70]

start_pos = 0
end_pos = 7
=>  [80, 70, 60, 50, 40, 30, 20, 10]

"""


def main():
    lst = [10, 20, 30, 40, 50, 60, 70, 80]
    pos = [
        (2, 4),
        (6, 7),
        (0, 7)
    ]

    for s, e in pos:
        print(lst[:s] + lst[s:e+1][::-1] + lst[e+1:])


if __name__ == "__main__":
    main()
