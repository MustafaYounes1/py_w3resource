"""

Write a Python program that implements a program that validates a user's password based on certain criteria
(length, containing numbers and special characters etc.) using boolean expressions.

Password length: 8-16
It must contain at least one digit, one capital letter, one lower-case letter, and one special character

afr12@hK$   =>  True
AQbg12Fert  =>  False

"""

from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def is_valid(s: str) -> bool:
    valid = 8 <= len(s) <= 16

    ps_s = set(s)
    valid = valid and bool(ps_s & set(ascii_lowercase))
    valid = valid and bool(ps_s & set(ascii_uppercase))
    valid = valid and bool(ps_s & set(digits))
    valid = valid and bool(ps_s & set(punctuation))

    return valid


def main():
    data = ["afr12@hK$", "AQbg12Fert"]

    for _ in data:
        print(is_valid(_))



if __name__ == "__main__":
    main()
