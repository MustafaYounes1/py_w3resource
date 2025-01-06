"""

Normalize the values in a list between 0 and 1 using the formula of Min-max scaling (z-score normalization):

    x' = (x -min) / (max -min)

lst = [2, 5, 10, 3, 8]      =>  [0.0, 0.375, 1.0, 0.125, 0.75]

"""


def main():
    lst = [2, 5, 10, 3, 8]
    mi = min(lst)
    ma = max(lst)
    print([(_ - mi) / (ma - mi) for _ in lst])


if __name__ == "__main__":
    main()
