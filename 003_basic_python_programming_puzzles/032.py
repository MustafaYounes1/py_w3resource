"""

Write a Python program to rescale and shift numbers in a given list, so that they cover the range [0, 1].

Note: Use Min-Max Scaling

Input:
[18.5, 17.0, 18.0, 19.0, 18.0]
Output:
[0.75, 0.0, 0.5, 1.0, 0.5]

Input:
[13.0, 17.0, 17.0, 15.5, 2.94]
Output:
[0.7155049786628734, 1.0, 1.0, 0.8933143669985776, 0.0]

"""


def main():
    seq = list(map(float, input("Enter a list of comma-separated floats: ").split(",")))
    mi, ma = min(seq), max(seq)
    print(
        [(_ - mi) / (ma - mi) for _ in seq]
    )


if __name__ == "__main__":
    main()
