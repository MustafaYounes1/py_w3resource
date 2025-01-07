"""

Write a Python program to convert a list into a nested dictionary of keys.

num_list = [1, 2, 3, 4]

{1: {2: {3: {4: {}}}}}

or in a more visually appealing format:

{
    1: {
        2: {
            3: {
                4: {}
            }
        }
    }
}

"""


def create_nested(lst):
    for idx, _ in enumerate(lst):
        if idx == len(lst) - 1:
            return {_: {}}
        else:
            return {_: create_nested(lst[idx+1:])}


def main():
    num_list = [1, 2, 3, 4]
    print(create_nested(num_list))


if __name__ == "__main__":
    main()
