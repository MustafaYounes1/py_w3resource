"""

Write a Python program that iterates over an enum class and displays each member and their value.

    Afghanistan -> 93
    Albania     -> 355
    Algeria     -> 213
    Andorra     -> 376
    Angola      -> 244
    Antarctica  -> 672

name: AFGHANISTAN , value:   93
name: ALBANIA     , value:  355
name: ALGERIA     , value:  213
name: ANDORRA     , value:  376
name: ANGOLA      , value:  244
name: ANTARCTICA  , value:  672

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
    for member in Country:
        print(f"name: {member.name:12}, value: {member.value:4}")


if __name__ == "__main__":
    main()
