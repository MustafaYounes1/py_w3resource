"""

Write a Python program to extract the first specified number of vowels from a given string. If the specified number
is less than the number of vowels present in the string then display "n is less than the number of vowels present in
the string".


("Python", 2)           -> "n is less than number of vowels present in the string."
("Python Exercises", 3) -> "oEe"
("AEIOU", 3)            -> "AEI"
"""


def main():
    data = [
        ("Python", 2),
        ("Python Exercises", 3),
        ("AEIOU", 3)
    ]

    for s, n in data:
        vowels = list(filter(lambda _: _.lower() in 'aeiou', s))
        if len(vowels) < n:
            print("n is less than number of vowels present in the string.")
        else:
            print("".join(vowels[:n]))


if __name__ == "__main__":
    main()
