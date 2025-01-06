"""

 Write a Python program to print letters from the English alphabet from a-z and A-Z.

a b c d e f g h i j k l m n o p q r s t u v w x y z
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

"""

from string import ascii_lowercase, ascii_uppercase


def main():
    print(" ".join([l for l in ascii_lowercase]))
    print(" ".join([l for l in ascii_uppercase]))


if __name__ == "__main__":
    main()
