"""

Write a Python program to find strings that, when case is flipped, give a target where vowels are replaced by
characters two later.

Input: Python           =>  pYTHQN
Input: aeiou            =>  CGKQW
Input: Hello, world!    =>  hGLLQ, WQRLD!
Input: AEIOU            =>  cgkqw

"""


def main():
    s = input("Enter a string: ")

    # Use the translate method to create a mapping for each vowel to the character two positions later
    translation_mapping = {ord(c): ord(c) + 2 for c in "aeiouAEIOU"}

    # Apply the translation mapping and swap the case of the characters in the string
    result = s.translate(translation_mapping).swapcase()

    print(result)


if __name__ == "__main__":
    main()
