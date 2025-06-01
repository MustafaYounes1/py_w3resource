"""

Write a Python program that creates a dictionary that maps food names to food namedtuple objects. Each food has a name
and a price.

"Pizza", 11.90
"Burger", 7.45
"Salad", 5.45

-> {
    'Pizza': Food(name='Pizza', price=11.9),
    'Burger': Food(name='Burger', price=7.45),
    'Salad': Food(name='Salad', price=5.45)
}

"""

from collections import namedtuple


def main():
    data = [
        ["Pizza", 11.90],
        ["Burger", 7.45],
        ["Salad", 5.45]
    ]

    food = namedtuple("Food", "name, price")
    m = {_[0]: food(*_) for _ in data}

    print(m)


if __name__ == "__main__":
    main()
