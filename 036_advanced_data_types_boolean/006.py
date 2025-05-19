"""

Write a Python function that checks if a given string is a palindrome (reads the same backward as forward) using
boolean values.

mamdam  =>  False
madam   =>  True

"""

def is_palindrome(s: str) -> bool:
    for a, b in zip(s, s[::-1]):
        if a != b:
            return False

    return True


def main():
    data = ["mamdam", "madam"]

    for _ in data:
        print(is_palindrome(_))


if __name__ == "__main__":
    main()
