"""

Write a Python program that takes a string with some words. For two consecutive words in the said string, check
whether the first word ends with a vowel and the next word begins with a vowel. If the program meets the condition,
 return true, otherwise false. Only one space is allowed between the words.

"These exercises can be used for practice."             -> True
"Following exercises should be removed for practice."   -> False
"I use these stories in my classroom."                  -> True

"""

import re


def main():
    data = [
        "These exercises can be used for practice.",
        "Following exercises should be removed for practice.",
        "I use these stories in my classroom."
    ]

    pa = re.compile(r"[aeiou]\s[aeiou]", flags=re.IGNORECASE)

    for _ in data:
        print(pa.search(_) is not None)


if __name__ == "__main__":
    main()
