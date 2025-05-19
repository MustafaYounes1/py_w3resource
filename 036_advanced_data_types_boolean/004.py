"""

Write a Python function that checks if a given list is empty or not using boolean logic.

[]  ->  True
[1] ->  False

"""

def is_list_empty(lst: list[...]) -> bool:
    return len(lst) == 0


def main():
    data = [
        [],
        [1]
    ]

    for _ in data:
        print(is_list_empty(_))


if __name__ == "__main__":
    main()
