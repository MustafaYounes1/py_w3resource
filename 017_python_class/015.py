"""

Write a Python class to check the validity of a string of parentheses, '(', ')', '{', '}', '[' and '].
These brackets must be closed in the correct order.
For example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.

(){}[]      =>  True
()[{)}      =>  False
({()})      =>  True
{{([])}}    =>  True
{{([))}}    False

"""


class ParenthesesValidity:
    __parentheses_map = {
        "(": ")",
        "{": "}",
        "[": "]",
    }

    @classmethod
    def check(cls, s: str) -> bool:
        tmp = []

        for _ in s:
            if _ in cls.__parentheses_map:
                tmp.append(_)

            elif _ == cls.__parentheses_map[tmp[-1]]:
                tmp.pop()

        return len(tmp) == 0


def main():
    data = ["(){}[]", "()[{)}", "({()})", "{{([])}}", "{{([))}}"]

    for _ in data:
        print(ParenthesesValidity.check(_))


if __name__ == "__main__":
    main()
