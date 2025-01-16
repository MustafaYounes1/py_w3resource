"""

Write a Python program to display all the member names of an enum class ordered by their values.

    Afghanistan -> 93
    Albania     -> 355
    Algeria     -> 213
    Andorra     -> 376
    Angola      -> 244
    Antarctica  -> 672

['AFGHANISTAN', 'ALGERIA', 'ANGOLA', 'ALBANIA', 'ANDORRA', 'ANTARCTICA']

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
    print([_.name for _ in sorted(Country)])


if __name__ == "__main__":
    main()
