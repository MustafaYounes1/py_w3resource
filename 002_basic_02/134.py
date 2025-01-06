"""

Write a Python program that alternates the case of each letter in a given string, with the first letter in the string
being uppercase.

Original string: Python Exercises
    =>  PyThOn ExErCiSeS

Original string: C# is used to develop web apps, desktop apps, mobile apps, games and much more.
    => C# iS uSeD tO dEvElOp WeB aPpS, dEsKtOp ApPs, MoBiLe ApPs, GaMeS aNd MuCh MoRe.

"""


def swap(txt):
    # Initialize an empty string to store the result.
    result_str = ""

    # Initialize a boolean variable 's' to determine whether to convert to uppercase or lowercase.
    s = True

    # Iterate through each character in the input string 'txt'.
    for i in txt:
        # If 's' is True, convert the character to uppercase; otherwise, convert it to lowercase.
        result_str += i.upper() if s else i.lower()

        # Toggle the value of 's' if the character is alphabetic.
        if i.isalpha():
            s = not s

    # Return the final result string with alternating case.
    return result_str


def main():
    s = input("Enter a string: ")
    out_s = swap(s)
    print(out_s)


if __name__ == "__main__":
    main()
