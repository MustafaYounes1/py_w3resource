"""

Write a Python program to print Emojis using Unicode characters or CLDR (Common Locale Data Repository) short names.

Note: The Common Locale Data Repository Project, often abbreviated as CLDR, is a project of the Unicode Consortium to
provide locale data in XML format for use in computer applications. CLDR contains locale-specific information that an
operating system will typically provide to applications.

unicode of Smiling face with heart-eyes: 0001F60D
unicode of Unamused face: 0001F612

"""


def main():
    print("\U0001F60D")
    print("\U0001F612")


if __name__ == "__main__":
    main()
