"""

Write a Python program to remove unwanted characters from a given string.

Original String : Pyth*^on Exercis^es   =>  Python Exercises
Original String : A%^!B#*CD             =>  ABCD


"""

from string import punctuation


def main():
    s = input("Enter a string: ")
    print("".join(list(filter(lambda _: _ not in punctuation, s))))


if __name__ == "__main__":
    main()
