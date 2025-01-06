"""

Write a Python program to hash a word.

"""


def main():
    word = input("Enter the word: ")
    print(hash(word))

    # or
    # # Create a list that maps characters to their Soundex codes.
    # soundex = [0, 1, 2, 3, 0, 1, 2, 0, 0, 2, 2, 4, 5, 5, 0, 1, 2, 6, 2, 3, 0, 1, 0, 2, 0, 2]
    #
    # # Prompt the user to input the word to be hashed.
    # word = input("Input the word to be hashed: ")
    #
    # # Convert the input word to uppercase.
    # word = word.upper()
    #
    # # Initialize the coded word with the first character of the input word.
    # coded = word[0]
    #
    # # Iterate over the remaining characters in the word to calculate the Soundex code.
    # for a in word[1:len(word)]:
    #     # Calculate the index for the Soundex list based on the character's ASCII code.
    #     i = 65 - ord(a)
    #     coded = coded + str(soundex[i])
    #
    # # Display the coded word.
    # print("The coded word is: " + coded)


if __name__ == "__main__":
    main()
