"""

Write a Python program to reverse only the vowels of a given string.

Sample Input:
"w3resource"    =>  w3resuorce
"Python"        =>  Python
"Perl"          =>  Perl
"USA"           =>  ASU
"hello"         =>  holle
"hello world"   =>  hollo werld

"""


def main():
    vowels = {'a', 'e', 'i', 'o', 'u'}
    s = input("Enter the string: ")
    vowels_pos = [idx for idx, c in enumerate(s) if c.lower() in vowels]

    curr_vowel_idx, out_str = -1, ""
    for idx, c in enumerate(s):
        if idx in vowels_pos:
            out_str += s[vowels_pos[curr_vowel_idx]]
            curr_vowel_idx -= 1
        else:
            out_str += c

    print(out_str)


if __name__ == "__main__":
    main()
