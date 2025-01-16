"""

Write a Python program to get unique enumeration values.

    Afghanistan -> 93
    Albania     -> 355
    Algeria     -> 213
    Andorra     -> 376
    Angola      -> 244
    Antarctica  -> 672
    India       -> 355
    USA         -> 213

AFGHANISTAN 93
ALBANIA    355
ALGERIA    213
ANDORRA    376
ANGOLA     244

Try to look up 355 value:  Country.ALBANIA
Try to look up INDIA name: Country.ALBANIA
Try to look up 213 value:  Country.ALGERIA
Try to look up USA name:   Country.ALGERIA


"""

from enum import Enum


class Country(Enum):
    AFGHANISTAN = 93
    ALBANIA = 355
    ALGERIA = 213
    ANDORRA = 376
    ANGOLA = 244
    INDIA = 355     # would behave as an alias to ALBANIA
    USA = 213       # would behave as an alias to ALGERIA


def main():
    for member in Country:
        print(f"{member.name:10} {member.value}")

    print(f"\nTry to look up 355 value:  {Country(355)}")
    print(f"Try to look up INDIA name: {Country['INDIA']}")

    print(f"Try to look up 213 value:  {Country(213)}")
    print(f"Try to look up USA name:   {Country['USA']}")

    # Note if you wanna break the aliasing property and throw errors when creating enums with non-unique values
    # use the enum.unique to decorate your enum


if __name__ == "__main__":
    main()
