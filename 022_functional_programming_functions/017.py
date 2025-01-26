"""

Write a Python program to create a chain of function decorators (bold, italic, underline etc.).
    bold(s)         =>  <b>s</b>
    italic(s)       =>  <i>s</i>
    underline(s)    =>  <u>s</u>
    Perform it in the following order: Underline -> Italic -> Bold

hello   =>  <b><i><u>hello world</u></i></b>

"""

from typing import Callable


def bold(func: Callable[..., str]) -> Callable[..., str]:
    def wrapper(*args, **kwargs) -> str:
        return "<b>" + func(*args, **kwargs) + "</b>"
    return wrapper


def italic(func: Callable[..., str]) -> Callable[..., str]:
    def wrapper(*args, **kwargs) -> str:
        return "<i>" + func(*args, **kwargs) + "</i>"
    return wrapper


def underline(func: Callable[..., str]) -> Callable[..., str]:
    def wrapper(*args, **kwargs) -> str:
        return "<u>" + func(*args, **kwargs) + "</u>"
    return wrapper


@bold
@italic
@underline
def test(s: str) -> str:
    return s


def main():
    print(test("hello"))


if __name__ == "__main__":
    main()
