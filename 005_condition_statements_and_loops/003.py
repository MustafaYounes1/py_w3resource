"""

Write a Python program to guess a number between 1 and 9.
Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess
is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

"""

import random


def main():
    n = random.randint(1, 9)
    u_n = int(input("Enter a number in [1, 9]: "))

    while True:
        if u_n == n:
            print("Well guessed!")
            break

        elif u_n > n:
            u_n = int(input("Try a smaller number in [1, 9]: "))

        else:
            u_n = int(input("Try a bigger number in [1, 9]: "))


if __name__ == "__main__":
    main()
