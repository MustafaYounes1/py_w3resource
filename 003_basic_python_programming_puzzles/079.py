"""

Write a Python program to find the largest negative and smallest positive numbers (or 0 if none).

[-12, -6, 300, -40, 2, 2, 3, 57, -50, -22, 12, 40, 9, 11, 18]       =>  [-6, 2]
[-1, -2, -3, -4]                                                    =>  [-1, 0]
[1, 2, 3, 4]                                                        =>  [0, 1]
[]                                                                  =>  [0, 0]

"""


def main():
    seq = list(map(int, input("Enter a list of comma-separated integers: ").split(",")))
    pos = [_ for _ in seq if _ > 0]
    neg = [_ for _ in seq if _ < 0]
    print(
        [
            max(neg) if neg else 0,
            min(pos) if pos else 0
        ]
    )


if __name__ == "__main__":
    main()
