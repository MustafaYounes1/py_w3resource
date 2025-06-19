"""

Write a Python program that creates a generator function that generates the next palindrome number after a given number.

0       =>  1
11      =>  22
55      =>  66
99      =>  101
112     =>  121

"""

from typing import Generator


def is_palindrome(n: int) -> bool:
    """Is the given integer palindrome?"""
    s = str(n)
    return s == s[::-1]


def palindrome_gen() -> Generator[int, int, None]:
    """Infinite palindrome number generator"""
    i = 0

    while True:
        if is_palindrome(i):
            sent_val = yield i

            if sent_val is not None:  # would be None when calling next or looping using for, or whatever was sent using .send
                i = sent_val

        i += 1


def get_next_palindrome(n: int) -> int:
    """Get the palindrome that follows n"""
    gen = palindrome_gen()
    next(gen)  # the generator must be started before calling .send using either next or .send(None)
    return gen.send(n)


def main():
    data = [0, 11, 55, 99, 112]

    for _ in data:
        print(get_next_palindrome(_))


if __name__ == "__main__":
    main()
