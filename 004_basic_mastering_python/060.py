"""

Filter a dictionary based on its values.

d = {'a': 1, 'b': 2, 'c': 3}
drop keys with values <= 1

{'b': 2, 'c': 3}

"""


def main():
    d = {'a': 1, 'b': 2, 'c': 3}
    print(
        {k: v for k, v in d.items() if v > 1}
    )


if __name__ == "__main__":
    main()
