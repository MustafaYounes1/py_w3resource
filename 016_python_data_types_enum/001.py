"""

Write a Python program to create the following Enum object

    Afghanistan -> 93
    Albania     -> 355
    Algeria     -> 213
    Andorra     -> 376
    Angola      -> 244
    Antarctica  -> 672

Display the name and value of the Enum member: Albania

"""

from enum import Enum


class Country(Enum):
    AFGHANISTAN = 93
    ALBANIA = 355
    ALGERIA = 213
    ANDORRA = 376
    ANGOLA = 244
    ANTARCTICA = 672


def main():
    print(Country.ALBANIA.name)
    print(Country.ALBANIA.value)


if __name__ == "__main__":
    main()
