"""

Write a Python program to get all values from an enum class.

    Afghanistan -> 93
    Albania     -> 355
    Algeria     -> 213
    Andorra     -> 376
    Angola      -> 244
    Antarctica  -> 672

[93, 355, 213, 376, 244, 672]

"""

from enum import IntEnum


class Country(IntEnum):
    AFGHANISTAN = 93
    ALBANIA = 355
    ALGERIA = 213
    ANDORRA = 376
    ANGOLA = 244
    ANTARCTICA = 672


def main():
    print(list(map(int, Country)))


if __name__ == "__main__":
    main()
