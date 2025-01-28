"""

Write a Python program that uses the filter function to extract all uppercase letters from a list of mixed-case strings.

["Hello", "w3resource", "Python", "Filter", "Learning"]     =>  ['H', 'P', 'F', 'L']

"""


def main():
    lst = ["Hello", "w3resource", "Python", "Filter", "Learning"]
    print(list(filter(lambda _: _.isupper(), "".join(lst))))


if __name__ == "__main__":
    main()
