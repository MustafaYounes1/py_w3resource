"""

Write a Python program to add member(s) to a set.

1. Start with an empty set
2. add "Red" to it
3. add the following collection of items to it ["Blue", "Green"]

{'Green', 'Red', 'Blue'}

"""


def main():
    s = set()
    s.add("Red")
    s.update(["Blue", "Green"])
    print(s)


if __name__ == "__main__":
    main()
