"""

Count the number of vowels in a string.

s = "hello world"   =>  3

"""


def main():
    vowels = 'aeiou'
    s = "hello world"
    print(len([_ for _ in s if _.lower() in vowels]))


if __name__ == "__main__":
    main()
