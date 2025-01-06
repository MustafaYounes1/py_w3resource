"""

Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg)
and atmosphere pressure.

    psi     = kPa / 6.89475729
    mmHg    = kPa * 760 / 101.325
    atm     = kPa / 101.325
"""


def main():
    kpa = float(input("Enter the pressure in kilopascals: "))
    print(f"psi:    {kpa / 6.89475729: 3f}")
    print(f"mmHg:   {kpa * 760 / 101.325: 3f}")
    print(f"atm:    {kpa / 101.325: 3f}")


if __name__ == "__main__":
    main()
