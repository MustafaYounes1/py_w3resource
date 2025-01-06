"""

Write a Python program to create a Caesar encryption.

Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift,
is one of the simplest and most widely known encryption techniques.

It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number
of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B,
and so on.

The method is named after Julius Caesar, who used it in his private correspondence.

abc     =>  cde

"""

from string import ascii_lowercase, ascii_uppercase


def main():
    s = input("Enter the text: ")
    shift = int(input("Enter the shift: "))
    print(
        "".join(
            [
                ascii_lowercase[ascii_lowercase.find(_) + shift] if _.islower() else ascii_uppercase[
                    ascii_uppercase.find(_) + shift] if _.lower() in ascii_lowercase else _ for _ in s
            ]
        )
    )


if __name__ == "__main__":
    main()
